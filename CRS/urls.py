
from django.urls import path, re_path
from . import views
from .views import QuestionAPI, ContainerAPI, ModelInputAPI, UserAPI, upload_image, CustomAuthToken

# URLConfiguration
urlpatterns = [
    path('', views.home, name='Home'),
    path('api/token/auth/', CustomAuthToken.as_view()),
    re_path('questions', QuestionAPI.as_view()),
    re_path('containers', ContainerAPI.as_view()),
    re_path('inputs', ModelInputAPI.as_view()),
    re_path('users', UserAPI.as_view()),
    path('upload_image/<int:pk>/', upload_image, name='upload_image'),
]
