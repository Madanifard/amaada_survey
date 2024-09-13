from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse


class SurveyAPITestCase(APITestCase):
    def setUp(self):
        # Set up initial data for the test
        self.client = APIClient()
        # Use the appropriate URL name
        self.survey_url = reverse('surveys_list_create')

        # Create some sample data
        self.survey_data = {
            'title': 'Customer Feedback Survey',
            'description': 'Survey for customer feedback',
        }

    def test_create_survey(self):
        # Create a survey via API
        response = self.client.post(
            self.survey_url, self.survey_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.survey_data['title'])

    def test_get_survey_list(self):
        # Get a list of surveys
        response = self.client.get(self.survey_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
