from rest_framework import serializers
from survey.models.responses import Responses


class ResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = ['id', 'user', 'question', 'option', 'answer_text']
