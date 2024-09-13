from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Surveys, Questions, Options, Responses, SurveyParticipants


class SurveyModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser",
                                        password="testpassword")
        self.survey = Surveys.objects.create(user=self.user,
                                             title="Sample Survey",
                                             description="A test survey",
                                             is_active=True)

    def test_multiple_choice_question(self):

        question = Questions.objects.create(survey=self.survey,
                                            text="What is your favorite?",
                                            type="multiple_choice")

        Options.objects.create(question=question,
                               key="color",
                               value={"values": [{"label": "Red", "order": 1},
                                                 {"label": "Blue", "order": 2},
                                                 {"label": "Green", "order": 3}]})

        self.assertEqual(Options.objects.filter(question=question).count(), 1)

    def test_matrix_question(self):

        question = Questions.objects.create(survey=self.survey,
                                            text="Rate the following statements",
                                            type="matrix")

        Options.objects.create(question=question,
                               key="rows",
                               value={"values": [{"label": "row1", "order": 1},
                                                 {"label": "row2", "order": 2}]})
        Options.objects.create(question=question,
                               key="columns",
                               value={"values": [{"label": "col1", "order": 1},
                                                 {"label": "col2", "order": 2}]})

        self.assertEqual(Options.objects.filter(question=question).count(), 2)

    def test_short_answer_question(self):

        question = Questions.objects.create(survey=self.survey,
                                            text="What is your name?",
                                            type="short_answer")

        response = Responses.objects.create(user=self.user,
                                            question=question,
                                            answer_text="John Doe",
                                            option=None)

        self.assertEqual(response.answer_text, "John Doe")

    def test_rating_question(self):

        question = Questions.objects.create(survey=self.survey,
                                            text="Rate our service",
                                            type="rating")

        Options.objects.create(question=question,
                               key="service1",
                               value={"rating": [1, 2, 3, 4]})
        Options.objects.create(question=question,
                               key="service2",
                               value={"rating": [10, 20, 30, 40]})

        self.assertEqual(Options.objects.filter(question=question).count(), 2)

    def test_survey_participation(self):
        SurveyParticipants.objects.create(survey=self.survey, user=self.user)

        self.assertEqual(SurveyParticipants.objects.filter(
            survey=self.survey).count(), 1)
