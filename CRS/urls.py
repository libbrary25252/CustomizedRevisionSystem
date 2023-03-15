
from django.urls import path, re_path
from . import views
# from .views import CategoryAPI

# URLConfiguration
urlpatterns = [
    path('', views.home, name='Home'),
    # re_path('categorys', CategoryAPI.as_view())
]
