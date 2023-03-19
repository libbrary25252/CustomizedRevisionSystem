from django.urls import path
from .views import ModelAPI

urlpatterns = [
    path('model/', ModelAPI.as_view(), name='topic_prediction'),
]
