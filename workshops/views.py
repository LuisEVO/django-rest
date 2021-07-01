from rest_framework import viewsets
from workshops.models import Workshop
from workshops.serializers import WorkshopModelSerializer
from rest_framework.permissions import IsAuthenticated


class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopModelSerializer
    permission_classes = [IsAuthenticated]
