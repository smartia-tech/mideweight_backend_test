from django.shortcuts import render
from rest_framework import viewsets
from .models import Posse, Gateway, GatewayStatus, GatewayTag
from .serializers import *
from .permissions import CustomDjangoModelPermissions
from .filtering import DynamicSearchFilter

# Create your views here.

class PosseViewSet(viewsets.ModelViewSet):
	filter_backends = (DynamicSearchFilter,)
	permission_classes = (CustomDjangoModelPermissions, )
	queryset = Posse.objects.all()
	serializer_class = PosseSerializer

class GatewayViewSet(viewsets.ModelViewSet):
	filter_backends = (DynamicSearchFilter,)
	permission_classes = (CustomDjangoModelPermissions, )
	queryset = Gateway.objects.all()
	serializer_class = GatewaySerializer

class GatewayStatusViewSet(viewsets.ModelViewSet):
	filter_backends = (DynamicSearchFilter,)
	permission_classes = (CustomDjangoModelPermissions, )
	queryset = GatewayStatus.objects.all()
	serializer_class = GatewayStatus

class GatewayTagViewSet(viewsets.ModelViewSet):
	filter_backends = (DynamicSearchFilter,)
	permission_classes = (CustomDjangoModelPermissions, )
	queryset = GatewayTag.objects.all()
	serializer_class = GatewayTag
