from django.db import models

class NLRequest(models.Model):
    request_str = models.TextField()

    def __str__(self):
        return self.request_ID


class Translation(models.Model):
    request = models.ForeignKey(NLRequest, on_delete=models.CASCADE)
    pred_CMD = models.TextField()
    score = models.DecimalField(max_digits=7, decimal_places=4)
    num_votes = models.PositiveIntegerField()