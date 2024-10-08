from django.db import models
from .questions import Questions


class Options(models.Model):
    question = models.ForeignKey(Questions,
                                 on_delete=models.CASCADE,
                                 related_name='options')
    key = models.CharField(max_length=256)
    value = models.JSONField()
