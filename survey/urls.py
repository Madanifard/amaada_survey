from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from survey.apis.survey import SurveysDetailAPIView, SurveysListCreateAPIView
from survey.apis.question import QuestionDetailAPIView, QuestionListCreateAPIView
from survey.apis.responses import ResponsesAPIView
from survey.apis.survey_participants import SurveyParticipantsAPIView

urlpatterns = [
    path('api/schema/',
         SpectacularAPIView.as_view(),
         name='schema'),

    path('api/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    path('api/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),

    path('user/<int:user_id>',
         SurveysListCreateAPIView.as_view(),
         name='surveys_list_create'),

    path('details/<int:pk>/user/<int:user_id>',
         SurveysDetailAPIView.as_view(),
         name='surveys_detail'),

    path('questions/',
         QuestionListCreateAPIView.as_view(),
         name='question_list_create'),

    path('questions/<int:question_id>/',
         QuestionDetailAPIView.as_view(),
         name='question_detail'),

    path('responses/',
         ResponsesAPIView.as_view(),
         name='responses'),

    path('responses/',
         ResponsesAPIView.as_view(),
         name='responses'),

    path('survey_participants/',
         SurveyParticipantsAPIView.as_view(),
         name='survey_participants'),
]
