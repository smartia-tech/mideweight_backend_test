from rest_framework.viewsets import ReadOnlyModelViewSet


from api.serializers import PosseSerializer
from data_sources.models import Posse


class PosseView(ReadOnlyModelViewSet):
    queryset = Posse.objects.all()
    serializer_class = PosseSerializer
