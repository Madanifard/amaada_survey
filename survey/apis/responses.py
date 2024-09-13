from django.http import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from survey.models.responses import Responses
from survey.serializers.response_serializer import ResponsesSerializer
from survey.celery_tasks.response_task import save_response_task


class ResponsesAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=ResponsesSerializer,
        responses={
            202: {'description': 'Response processing task is running.'},
            400: {'description': 'Invalid input data.'}
        },
        summary="Submit a response asynchronously",
        description="Submit a new response to a survey or question. If the input data is valid, the task is queued and a 202 status is returned. In case of invalid data, a 400 error is returned."
    )
    def post(self, request: HttpRequest):
        """
            Handle POST request to submit a new response asynchronously.

            Args:
            - request (HttpRequest): The incoming HTTP request containing response data.

            Returns:
            - Response: A message indicating the task is running with a 202 status, or a 400 error if the input is invalid.
        """
        serializer = ResponsesSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user'].id
            question_id = serializer.validated_data['question'].id
            option_id = serializer.validated_data['option'].id
            answer_text = serializer.validated_data['answer_text']

            save_response_task.delay(user_id,
                                     question_id,
                                     option_id,
                                     answer_text)

            return Response({"status": "Task is running"}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
