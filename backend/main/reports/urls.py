from rest_framework import routers
from reports.views import IncidentReportViewset


router = routers.SimpleRouter()
router.register("", IncidentReportViewset,'incidentreport')
