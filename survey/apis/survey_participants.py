from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from survey.models.survey_participants import SurveyParticipants
from survey.serializers.survey_participants import SurveyParticipantsSerializer


class SurveyParticipantsAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=SurveyParticipantsSerializer,
        responses={
            201: SurveyParticipantsSerializer,
            400: {'description': 'Invalid input data.'}
        },
        summary="Add a participant to a survey",
        description="Add a new participant to a survey with the provided data. If the input is valid, the participant is saved, and a 201 status is returned. In case of invalid data, a 400 error is returned."
    )
    def post(self, request):
        """
            Handle POST request to add a new participant to a survey.

            Args:
            - request (HttpRequest): The incoming HTTP request containing participant data.

            Returns:
            - Response: A JSON object of the created participant with a 201 status, or a 400 error if the input data is invalid.
        """
        serializer = SurveyParticipantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
