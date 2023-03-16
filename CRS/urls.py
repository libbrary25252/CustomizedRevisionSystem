
from django.urls import path, re_path
from . import views
from .views import QuestionAPI

# URLConfiguration
urlpatterns = [
    path('', views.home, name='Home'),
    re_path('questions', QuestionAPI.as_view())
]
