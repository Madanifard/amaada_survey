from django.db import models
from django.contrib.auth.models import User
from .surveys import Surveys


class SurveyParticipants(models.Model):
    survey = models.ForeignKey(Surveys, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)