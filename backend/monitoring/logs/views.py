from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from monitoring.settings import DEFAULT_PAGINATION_LIMIT

from logs.models import Log
from logs.serializers import LogSerializer


class CustomOffsetPagination(LimitOffsetPagination):
    offset_query_param = "start"
    default_limit = DEFAULT_PAGINATION_LIMIT


class LogsViewset(mixins.ListModelMixin, GenericViewSet):
    """
    A view for listing all logs
    """

    queryset = Log.objects.all()
    serializer_class = LogSerializer
    pagination_class = CustomOffsetPagination