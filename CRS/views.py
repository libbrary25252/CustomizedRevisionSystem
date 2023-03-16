from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, QuestionQuestion
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from .serializers import QuestionSerializer, ContainerSerializer

def home(request):
    return render(request, 'home.html', {'name': 'Hello'})

class QuestionAPI(APIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        questions = Question.objects.all()
        return questions

    def get(self, request, *args, **kwargs):
        try:
            ID = request.query_param["QID"]
            parentID = request.query_param["parentQID"]
            statement = request.query_param["statement"]
            string = request.query_param["string"]
            Qtype = request.query_param["Qtype"]
            imagefile = request.query_param["image"]
            description = request.query_param["description"]
            option = request.query_param["description"]
            catergory = request.query_param["category"]
            if ID != None:
                ID = Question.objects.get(QID=ID)
                serializer = QuestionSerializer(ID)
            if string != None:
                string = Question.objects.get(string=string)
                serializer = QuestionSerializer(string)
            if Qtype != None:
                Qtype = Question.objects.get(Qtype=Qtype)
                serializer = QuestionSerializer(Qtype)
        except:
            questions = self.get_queryset()
            serializer = QuestionSerializer(questions, many=True) #get all
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        question_data = request.data
        new_question = Question.objects.create(QID=question_data["QID"], statement=question_data["statement"], string=question_data["string"], Qtype=question_data["Qtype"], description=question_data["description"], options=question_data["options"])
        new_question.save()
        serializer = QuestionSerializer(new_question)
        return Response(serializer.data)
    
    class ContainerAPI(APIView):
        serializer_class = ContainerSerializer

    def get_queryset(self):
        containers = QuestionQuestion.objects.all()
        return containers

    def get(self, request, *args, **kwargs):
        try:
            state_id = request.query_param["state_id"]
            statement = request.query_param["statement"]
            qid = request.query_param["qid"]
            
            if state_id != None:
                state_id = QuestionQuestion.objects.get(state_id=state_id)
                serializer = ContainerSerializer(state_id)
            if statement != None:
                statement = QuestionQuestion.objects.get(statement=statement)
                serializer = ContainerSerializer(statement)
            if qid != None:
                qid = QuestionQuestion.objects.get(qid=qid)
                serializer = ContainerSerializer(qid)
        except:
            containers = self.get_queryset()
            serializer = ContainerSerializer(containers, many=True) #get all
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        container_data = request.data
        new_container = Question.objects.create(state_id=container_data["state_id"], statement=container_data["statement"], qid=container_data["qid"])
        new_container.save()
        serializer = ContainerSerializer(new_container)
        return Response(serializer.data)