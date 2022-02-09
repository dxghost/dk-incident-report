from django.db import models

LOG_MESSAGE_MAX_LEN = 200


class Log(models.Model):
    message = models.CharField(max_length=LOG_MESSAGE_MAX_LEN)

    def __str__(self):
        return "({}, {})".format(self.pk, self.message)
