from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid

from .serializers import CategorySerializer

def home(request):
    return render(request, 'home.html', {'name': 'Hello'})

class CategoryAPI(APIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        catergorys = Category.objects.all()
        return catergorys

    def get(self, request, *args, **kwargs):
        try:
            c_name = request.query_param["c_name"]
            if c_name != None:
                catergory = Category.objects.get(c_name=c_name)
                serializer = CategorySerializer(catergory)
        except:
            catergorys = self.get_queryset()
            serializer = CategorySerializer(catergorys, many=True) #get all
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        category_data = request.data
        new_category = Category.objects.create(c_id=category_data["c_id"],c_name=category_data["c_name"], description=category_data["description"])
        new_category.save()
        serializer = CategorySerializer(new_category)
        return Response(serializer.data)