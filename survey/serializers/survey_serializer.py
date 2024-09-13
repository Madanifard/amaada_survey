from rest_framework import serializers
from survey.models.surveys import Surveys
from survey.serializers.question_serializer import QuestionSerializer


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Surveys
        fields = ['id', 'user', 'title',
                  'description', 'is_active',
                  'created_at', 'questions']
