from django.db import models
from django.contrib.auth.models import User
from .questions import Questions
from .options import Options


class Responses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option = models.ForeignKey(Options, on_delete=models.CASCADE)
    answer_text = models.TextField()