from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from faker import Faker
from logs.models import Log
from monitoring.settings import DEFAULT_PAGINATION_LIMIT
from logs.models import LOG_MESSAGE_MAX_LEN
from logs.views import CustomOffsetPagination
from django.utils.http import urlencode


class LogTestCase(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.client = APIClient()

    def test_view_report_list_offset(self):
        for _ in range(DEFAULT_PAGINATION_LIMIT * 3):
            msg = self.faker.text(LOG_MESSAGE_MAX_LEN)
            Log.objects.create(message=msg)
        params = {CustomOffsetPagination.offset_query_param: DEFAULT_PAGINATION_LIMIT}
        url = "{}?{}".format(reverse("logs-list"), urlencode(params))
        response = self.client.get(url)
        self.assertEqual(response.data.get("results")[0].get("id"),DEFAULT_PAGINATION_LIMIT+1)
        self.assertEqual(len(response.data.get("results")),DEFAULT_PAGINATION_LIMIT)
