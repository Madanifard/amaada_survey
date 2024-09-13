from django.db import models
from .surveys import Surveys


class Questions(models.Model):
    survey = models.ForeignKey(Surveys,
                               related_name='questions',
                               on_delete=models.CASCADE)
    text = models.TextField()
    type = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title
