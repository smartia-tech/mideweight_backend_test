from .serializers import (GatewaySerializer,
                          GatewayTagSerializer,
                          GatewayStatusSerializer,
                          PosseSerializer)
from .models import (Gateway,
                     GatewayTag,
                     GatewayStatus,
                     Posse)
from .utils import CustomViewSet
from .redoc import CustomAutoSchema


# Check .utils folder for more info :)

# Customizing the docs
class GatewaySchema(CustomAutoSchema):
    python_template = ''
    js_template = ''
    rust_template = ''


# Create your views here.

class GatewayView(CustomViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer
    filterset_fields = ['posse', 'serial_number', 'location', 'label']


class GatewayTagView(CustomViewSet):
    queryset = GatewayTag.objects.all()
    serializer_class = GatewayTagSerializer
    filterset_fields = ['status', 'unit_type', 'hardware_name']


class GatewayStatusView(CustomViewSet):
    queryset = GatewayStatus.objects.all()
    serializer_class = GatewayStatusSerializer
    filterset_fields = ['data_flow', 'os_name', 'os_version']


class PosseView(CustomViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
    # filterset_fields = ['level']
