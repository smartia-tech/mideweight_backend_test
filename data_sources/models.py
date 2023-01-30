from django.core.validators import MinLengthValidator
from django.db import models


class DataSourceBaseModel(models.Model):
    class Meta:
        abstract = True


class Posse(DataSourceBaseModel):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class DataSource(DataSourceBaseModel):
    label = models.CharField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # The type name will be used in the situations that a user can choose
    # a list of available data sources.
    # Type name must be implemented by subclass
    type_name = None

    class Meta:
        abstract = True

    def __str__(self):
        return self.label


class Gateway(DataSource):
    label = models.CharField(max_length=100,
                             validators=[MinLengthValidator(limit_value=3)])
    posse = models.ForeignKey(Posse, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)  # Removal with #2mcytb
    # TODO(#2pfzca): Verify the correctness of client_id when saving
    # The above concern comes if a user entered a wrong client_id but the id
    # is invalid, then the Gateway will not be able to connect with
    # maio-engine.
    oauth2_client_id = models.CharField(max_length=100, unique=True)
    serial_number = models.CharField(
        max_length=255, validators=[MinLengthValidator(limit_value=3)])
    type_name = "Machine Gateway"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['label', 'serial_number'],
                                    name="label_serial_number")
        ]

    @property
    def queue_name(self):
        return 'gateway_{serial}_{id}'.format(serial=self.serial_number,
                                              id=self.id)

    @property
    def tags(self):
        return self.gatewaytag_set.all()

    @property
    def data_flow(self) -> bool:
        gateway_status = self.gatewaystatus_set.filter(gateway_id=self.id)
        if gateway_status.count() > 0:
            return gateway_status.latest('created_at').data_flow
        return False


class GatewayStatus(DataSourceBaseModel):
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=255,
                                validators=[MinLengthValidator(limit_value=3)])
    data_flow = models.BooleanField()
    os_name = models.CharField(max_length=255)
    os_version = models.CharField(max_length=255)
    firmware_version = models.CharField(max_length=255)
    maio_edge_version = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'


class AbstractTag(DataSourceBaseModel):
    label = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def datasource(self) -> DataSource:
        """The data source this tag is a associated with"""
        raise NotImplementedError("must be implemented by subclass")


class GatewayTag(AbstractTag):
    UNIT_TYPES = (
        ('bool', 'Boolean'),
        ('float', 'Float'),
        ('int', 'Integer'),
        ('str', 'String'),
    )
    STATUSES = (
        ('active', 'Active'),
        ('disabled', 'Disabled'),
        ('dormant', 'Dormant'),
    )
    gateway = models.ForeignKey(Gateway, on_delete=models.CASCADE)
    data_flow = models.BooleanField()
    hardware_name = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255, blank=True)
    unit_type = models.CharField(max_length=255, choices=UNIT_TYPES)
    status = models.CharField(default="active",
                              choices=STATUSES,
                              max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['gateway_id', 'label'],
                                    name="gateway and label "
                                    "should be unique in GatewayTag."),
            models.UniqueConstraint(fields=['gateway_id', 'hardware_name'],
                                    name="gateway and hardware_name "
                                    "should be unique in GatewayTag."),
        ]

    def __str__(self):
        return self.label

    @property
    def datasource(self) -> DataSource:
        return self.gateway
