from survey.models.questions import Questions
from survey.models.options import Options
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class QuestionAPITestCase(APITestCase):

    def setUp(self):
        """
        Set up test data
        """
        # Create a question and options
        self.question = Questions.objects.create(
            survey="Survey 1", text="What is your favorite color?", type="multiple_choice")

        self.option1 = Options.objects.create(
            question=self.question, key="A", value="Red")
        self.option2 = Options.objects.create(
            question=self.question, key="B", value="Blue")

        # Define URLs
        self.question_list_url = reverse('question_list_create')
        self.question_detail_url = reverse(
            'question_detail', args=[self.question.id])

    def test_get_questions(self):
        """
        Test retrieving the list of questions
        """
        response = self.client.get(self.question_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # One question should be returned
        self.assertEqual(len(response.data), 1)

    def test_post_question(self):
        """
        Test creating a new question
        """
        data = {
            "survey": "Survey 2",
            "text": "What is your favorite fruit?",
            "type": "multiple_choice",
            "options": [
                {"key": "A", "value": "Apple"},
                {"key": "B", "value": "Banana"}
            ]
        }
        response = self.client.post(
            self.question_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['text'], "What is your favorite fruit?")
        self.assertEqual(len(response.data['options']), 2)

    def test_get_question_detail(self):
        """
        Test retrieving a specific question
        """
        response = self.client.get(self.question_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.question.text)

    def test_put_question(self):
        """
        Test updating a specific question
        """
        data = {
            "survey": "Survey 1",
            "text": "What is your favorite animal?",
            "type": "multiple_choice",
            "options": [
                {"id": self.option1.id, "key": "A", "value": "Cat"},
                {"id": self.option2, "key": "B", "value": "Dog"}
            ]
        }
        response = self.client.put(
            self.question_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'],
                         "What is your favorite animal?")
        self.assertEqual(len(response.data['options']), 2)
        self.assertEqual(response.data['options'][0]['value'], "Cat")

    def test_delete_question(self):
        """
        Test deleting a specific question
        """
        response = self.client.delete(self.question_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Ensure the question is deleted
        self.assertFalse(Questions.objects.filter(
            id=self.question.id).exists())
