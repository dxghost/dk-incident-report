from django.db import models

REPORT_MESSAGE_MAX_LEN = 200

class IncidentReport(models.Model):
    message = models.CharField(max_length=REPORT_MESSAGE_MAX_LEN)

    def __str__(self):
        return "({}, {})".format(self.pk, self.message)

def store_multiple_reports(task):
    datas = task.result
    for dt in datas:
        msg = dt["message"]
        IncidentReport.objects.create(message=msg)
    print(datas)