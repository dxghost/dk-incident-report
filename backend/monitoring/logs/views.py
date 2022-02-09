from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from logs.models import Log
from logs.serializers import LogSerializer


class CustomOffsetPagination(LimitOffsetPagination):
    offset_query_param = "start"
    default_limit = 15


class LogsViewset(mixins.ListModelMixin, GenericViewSet):
    """
    A view for listing all logs
    """

    queryset = Log.objects.all()
    serializer_class = LogSerializer
    pagination_class = CustomOffsetPagination