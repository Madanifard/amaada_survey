from django.http import HttpRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from survey.models.surveys import Surveys
from survey.serializers.survey_serializer import SurveySerializer


class SurveysListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        responses={
            200: SurveySerializer(many=True),
        },
        summary="Retrieve all questionnaires",
        description=(
            "Retrieve all questionnaires associated with a specific user ID.\n"
        ),
    )
    def get(self, request: HttpRequest, user_id: int) -> Response:
        """
            Retrieve all questionnaires associated with a specific user ID.

            Args:
                request (HttpRequest): The HTTP request object.
                user_id (int): The ID of the user for whom to retrieve questionnaires.

            Returns:
                Response: A Response object containing a JSON list of questionnaires for the specified user.
        """
        surveys = Surveys.objects.filter(user=user_id)
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

    @extend_schema(
        request=SurveySerializer,
        responses={
            201: SurveySerializer,
            400: OpenApiTypes.OBJECT
        },
        summary="Create a new survey",
        description=(
            "Create a new survey associated with a specific user ID.\n\n"
            "The request should contain the following parameters:\n"
            "- title (str): The title of the survey.\n"
            "- description (str): A description of the survey.\n"
            "- is_active (bool): The status indicating if the survey is active."
        ),
    )
    def post(self, request: HttpRequest, user_id: int) -> Response:
        """
            Create a new survey associated with a specific user ID.

            The request should contain the following parameters:
            - title (str): The title of the survey.
            - description (str): A description of the survey.
            - is_active (bool): The status indicating if the survey is active.

            Args:
                request (HttpRequest): The HTTP request object containing survey data.
                user_id (int): The ID of the user to whom the survey will be associated.

            Returns:
                Response: A Response object containing the serialized survey data if creation is successful,
                        or validation errors if the request data is invalid. The status code is 201 for
                        successful creation and 400 for validation errors.
        """
        data = request.data.copy()
        data['user'] = user_id
        serializer = SurveySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveysDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        responses={
            200: SurveySerializer,
            404: {'description': 'Survey not found.'}
        },
        summary="Retrieve survey details",
        description="Fetch a survey by its primary key for the authenticated user. If the survey is not found, a 404 error is returned."
    )
    def get(self, request: HttpRequest, pk: int, user_id: int) -> Response:
        """
            Handle GET request to retrieve a specific survey for the authenticated user.

            Args:
            - request (HttpRequest): The incoming HTTP request.
            - pk (int): The primary key of the survey to retrieve.
            - user_id (int): The ID of the user for whom to retrieve questionnaires.

            Returns:
            - Response: A JSON object containing the survey details or a 404 error if not found.
        """
        try:
            survey = Surveys.objects.get(pk=pk, user=user_id)
        except Surveys.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SurveySerializer(survey)
        return Response(serializer.data)

    @extend_schema(
        request=SurveySerializer,
        responses={
            200: SurveySerializer,
            400: {'description': 'Invalid input data.'},
            404: {'description': 'Survey not found.'}
        },
        summary="Update survey details",
        description="Update the details of an existing survey for the authenticated user by providing a valid primary key and data."
    )
    def put(self, request: HttpRequest, pk: int, user_id: int) -> Response:
        """
            Handle PUT request to update a specific survey for the authenticated user.

            The request should contain the following parameters:
            - title (str): The title of the survey.
            - description (str): A description of the survey.
            - is_active (bool): The status indicating if the survey is active.

            Args:
            - request (HttpRequest): The incoming HTTP request with updated survey data.
            - pk (int): The primary key of the survey to update.
            - user_id (int): The ID of the user for whom to retrieve questionnaires.

            Returns:
            - Response: A JSON object containing the updated survey details or an error message.
        """

        try:
            survey = Surveys.objects.get(pk=pk, user=user_id)
        except Surveys.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['user'] = user_id
        serializer = SurveySerializer(survey,
                                      data=data,
                                      partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={
            204: None,
            404: {'description': 'Survey not found.'}
        },
        summary="Delete a survey",
        description="Delete a survey by its primary key and user ID. If the survey is not found, a 404 error is returned."
    )
    def delete(self, request: HttpRequest, pk: int, user_id: int) -> Response:
        """
            Handle DELETE request to remove a specific survey for a given user.

            Args:
            - request (HttpRequest): The incoming HTTP request.
            - pk (int): The primary key of the survey to delete.
            - user_id (int): The ID of the user who owns the survey.

            Returns:
            - Response: A 204 No Content status on success or 404 Not Found if the survey does not exist.
        """
        try:
            survey = Surveys.objects.get(pk=pk, user=user_id)
        except Surveys.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
