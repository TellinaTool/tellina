from django.db import models
from django.utils import timezone

class NLRequest(models.Model):
    """
    A natural language request issued by the user.
    :member request_str: the natural language string issued by the user
    :member submission_time: the time when the natural language request is
        submitted
    :member frequency: number of times the query has been issued
    """
    request_str = models.TextField()
    submission_time = models.DateTimeField(default=timezone.now)
    frequency = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.request_str

    def inc_frequency(self):
        self.frequency += 1
        self.save()


class Translation(models.Model):
    request = models.ForeignKey(NLRequest, on_delete=models.CASCADE)
    pred_cmd = models.TextField()
    score = models.FloatField()
    num_votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{}\n{}".format(self.request, self.pred_cmd)


class NLRequestIPAddress(models.Model):
    """
    Memorize the queries issued from specific IP addresses.
    :member request: a natural language request
    :member ip_address: the user's ip address
    """
    request = models.ForeignKey(NLRequest, on_delete=models.CASCADE)
    ip_address = models.TextField(default='')
