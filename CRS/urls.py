
from django.urls import path, re_path
from . import views
from .views import QuestionAPI, ContainerAPI, ModelInputAPI

# URLConfiguration
urlpatterns = [
    path('', views.home, name='Home'),
    re_path('questions', QuestionAPI.as_view(),),
    re_path('containers', ContainerAPI.as_view()),
    re_path('inputs', ModelInputAPI.as_view()),

]
