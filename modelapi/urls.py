
from django.urls import path, re_path
from . import views
from .views import ModelAPI

# URLConfiguration
urlpatterns = [
    re_path('api', ModelAPI.as_view()),
]
