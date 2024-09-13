from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from survey.models.options import Questions
from survey.serializers.question_serializer import QuestionSerializer


class QuestionListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        responses={
            200: QuestionSerializer(many=True)
        },
        summary="List all questions",
        description="Retrieve a list of all questions stored in the database."
    )
    def get(self, request: HttpRequest) -> Response:
        """
            Handle GET request to retrieve a list of all questions.

            Args:
            - request (HttpRequest): The incoming HTTP request.

            Returns:
            - Response: A list of questions in JSON format.
        """
        questions = Questions.objects.all().prefetch_related('options')
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=QuestionSerializer,
        responses={
            201: QuestionSerializer,
            400: {'description': 'Invalid input data.'}
        },
        summary="Create a new question",
        description="Create a new question in the database if the input data is valid."
    )
    def post(self, request: HttpRequest) -> Response:
        """
            Handle POST request to create a new question.

            Args:
            - request (HttpRequest): The incoming HTTP request containing the new question data.

            Returns:
            - Response: The created question in JSON format, or an error message if the data is invalid.
        """
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        responses={
            200: QuestionSerializer,
            404: {'description': 'Question not found.'}
        },
        summary="Retrieve a specific question",
        description="Fetch a question by its ID. If the question is not found, a 404 error is returned."
    )
    def get(self, request: HttpRequest, question_id: int) -> Response:
        """
            Handle GET request to retrieve a specific question by its ID.

            Args:
            - request (HttpRequest): The incoming HTTP request.
            - question_id (int): The ID of the question to retrieve.

            Returns:
            - Response: A JSON object containing the question details or a 404 error if not found.
        """
        try:
            question = Questions.objects.get(pk=question_id)
        except Questions.DoesNotExist:
            return Response({'description': 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    @extend_schema(
        request=QuestionSerializer,
        responses={
            200: QuestionSerializer,
            400: {'description': 'Invalid input data.'},
            404: {'description': 'Question not found.'}
        },
        summary="Update a specific question",
        description="Update a question's details by providing its ID and the new data. If the question is not found, a 404 error is returned."
    )
    def put(self, request: HttpRequest, question_id: int) -> Response:
        """
            Handle PUT request to update a specific question by its ID.

            Args:
            - request (HttpRequest): The incoming HTTP request with updated question data.
            - question_id (int): The ID of the question to update.

            Returns:
            - Response: A JSON object containing the updated question or an error message if invalid data is provided or the question is not found.
        """
        try:
            question = Questions.objects.get(pk=question_id)
        except Questions.DoesNotExist:
            return Response({'description': 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={
            204: None,
            404: {'description': 'Question not found.'}
        },
        summary="Delete a specific question",
        description="Delete a question by its ID. If the question is not found, a 404 error is returned."
    )
    def delete(self, request: HttpRequest, question_id: int) -> Response:
        """
            Handle DELETE request to remove a specific question by its ID.

            Args:
            - request (HttpRequest): The incoming HTTP request.
            - question_id (int): The ID of the question to delete.

            Returns:
            - Response: A 204 No Content status on success or a 404 error if the question is not found.
        """
        try:
            question = Questions.objects.get(pk=question_id)
        except Questions.DoesNotExist:
            return Response({'description': 'Question not found.'}, status=status.HTTP_404_NOT_FOUND)

        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
