from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from survey.apis.survey import SurveysDetailAPIView, SurveysListCreateAPIView
from survey.apis.question import QuestionDetailAPIView, QuestionListCreateAPIView

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
         name='surveys-list-create'),

    path('details/<int:pk>/user/<int:user_id>',
         SurveysDetailAPIView.as_view(),
         name='surveys-detail'),

    path('questions/',
         QuestionListCreateAPIView.as_view(),
         name='question-list-create'),

    path('questions/<int:question_id>/',
         QuestionDetailAPIView.as_view(),
         name='question-detail'),
]
