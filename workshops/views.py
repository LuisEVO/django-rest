from xmlrpc.client import Server

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from workshops.models import Workshop
from workshops.serializers import WorkshopModelSerializer, WorkshopCoverPageModelSerializer,\
    WorkshopTemaryModelSerializer
from rest_framework.permissions import IsAuthenticated


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class WorkshopsPaginatedViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopModelSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination


class WorkshopsViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopModelSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = LargeResultsSetPagination


class WorkshopsCoverPageViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopCoverPageModelSerializer
    # permission_classes = [IsAuthenticated]


class WorkshopsTemaryViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopTemaryModelSerializer
    # permission_classes = [IsAuthenticated]


