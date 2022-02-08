from django.test import TestCase
from django.db.utils import DataError
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from faker import Faker
from reports.models import IncidentReport, REPORT_MESSAGE_MAX_LEN


class IncidentReportTestCase(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.client = APIClient()

    def test_model_report_creation(self):
        msg = self.faker.text(REPORT_MESSAGE_MAX_LEN)
        IncidentReport.objects.create(message=msg)
        got = IncidentReport.objects.latest("pk")
        self.assertEqual(msg, got.message)

    def test_model_report_validation(self):
        msg = self.faker.pystr(
            min_chars=REPORT_MESSAGE_MAX_LEN + 1, 
            max_chars=REPORT_MESSAGE_MAX_LEN + 2
        )
        with self.assertRaises(DataError):
            IncidentReport.objects.create(message=msg)

    def test_view_report_list(self):
        msg = self.faker.text(REPORT_MESSAGE_MAX_LEN)
        IncidentReport.objects.create(message=msg)
        response = self.client.get(reverse('incidentreport-list'))
        self.assertEqual(response.data[0]["message"], msg)
