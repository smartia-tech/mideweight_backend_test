from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

"""

This custom view helps to create a uniform response for for both successful and failed requests,
this makes consumption on the frontend a lot more easier.

"""


class CustomViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"status": "Success",
                             "code": 201,
                             "message": serializer.data},
                            status=status.HTTP_201_CREATED,
                            headers=headers,
                            content_type='json')
        except APIException as err:

            return Response({"status": "Failed",
                             "code": 400,
                             "message": err.detail},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type='json')

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({"status": "Success",
                             "code": 200,
                             "message": serializer.data},
                            status=status.HTTP_200_OK,
                            content_type='json')
        except APIException as err:

            return Response({"status": "Failed",
                             "code": 400,
                             "message": err.detail},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type='json')
