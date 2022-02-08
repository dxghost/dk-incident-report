from django.db import models

REPORT_MESSAGE_MAX_LEN = 200

class IncidentReport(models.Model):
    message = models.CharField(max_length=REPORT_MESSAGE_MAX_LEN)

    def __str__(self):
        return "({}, {})".format(self.pk, self.message)
