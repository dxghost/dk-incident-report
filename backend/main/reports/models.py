from django.db import models


class IncidentReport(models.Model):
    message = models.CharField(max_length=200)

    def __str__(self):
        return "({}, {})".format(self.pk, self.message)
