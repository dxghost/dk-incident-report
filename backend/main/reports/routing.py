from django.urls import path
from reports.consumers import ReportConsumer

ws_urlpatterns = [
    path("reports/",ReportConsumer.as_asgi())
]