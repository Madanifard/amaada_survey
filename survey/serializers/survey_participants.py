from rest_framework import serializers
from survey.models.survey_participants import SurveyParticipants


class SurveyParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyParticipants
        fields = ['id', 'survey', 'user', 'submitted_at']
