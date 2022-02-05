from rest_framework import serializers
from reports.models import IncidentReport


class IncidentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentReport
        fields = "__all__"
