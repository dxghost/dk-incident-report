from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from reports.models import IncidentReport
from reports.serializer import IncidentReportSerializer


class IncidentReportViewset(mixins.ListModelMixin, GenericViewSet):
    """
    A view for listing all incident reports
    """

    queryset = IncidentReport.objects.all()
    serializer_class = IncidentReportSerializer
