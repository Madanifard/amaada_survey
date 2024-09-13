from rest_framework import serializers
from survey.models.surveys import Surveys


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveys
        fields = ['id', 'user', 'title',
                  'description', 'is_active', 'created_at']
