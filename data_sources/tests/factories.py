import factory

from data_sources.models import Posse, Gateway, GatewayStatus, GatewayTag


class PosseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Posse


class GatewayFactory(factory.django.DjangoModelFactory):
    posse = factory.SubFactory(PosseFactory)
    label = factory.Faker('sentence', nb_words=1)
    serial_number = factory.Sequence(lambda n: 100 + n)
    oauth2_client_id = factory.Sequence(lambda x: 100 + x)

    class Meta:
        model = Gateway


class GatewayTagFactory(factory.django.DjangoModelFactory):
    gateway = factory.SubFactory(GatewayFactory)
    hardware_name = factory.Faker('sentence', nb_words=1)
    data_flow = True

    class Meta:
        model = GatewayTag


class GatewayStatusFactory(factory.django.DjangoModelFactory):
    gateway = factory.SubFactory(GatewayFactory)
    os_version = factory.Sequence(lambda n: f"1.6.{n}")
    data_flow = True

    class Meta:
        model = GatewayStatus
