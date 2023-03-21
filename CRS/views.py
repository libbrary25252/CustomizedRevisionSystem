from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, QuestionQuestion, QuestionInput
from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
import datetime
from .serializers import QuestionSerializer, ContainerSerializer, InputSerializer


def home(request):
    return render(request, 'home.html', {'name': 'Hello'})


def genSeqID(uid, sequence):
    time = datetime.datetime.now()
    str_time = str(time).replace("-", "").replace(" ", "").replace(":", "")
    str_time = str_time[:str_time.rfind('.')]
    res = uid + "-" + str_time + "-" + str(sequence)
    print(res)
    return res


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
            serializer = QuestionSerializer(questions, many=True)  # get all
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        question_data = request.data
        new_question = Question.objects.create(QID=question_data["QID"], statement=question_data["statement"], string=question_data["string"],
                                               Qtype=question_data["Qtype"], description=question_data["description"], options=question_data["options"])
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
            serializer = ContainerSerializer(containers, many=True)  # get all
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        container_data = request.data
        new_container = QuestionQuestion.objects.create(
            state_id=container_data["state_id"], statement=container_data["statement"], qid=container_data["qid"])
        new_container.save()
        serializer = ContainerSerializer(new_container)
        return Response(serializer.data)


class ModelInputAPI(APIView):
    serializer_class = InputSerializer

    def get_queryset(self):
        quesinputs = QuestionInput.objects.all()
        return quesinputs

    def get(self, request, *args, **kwargs):
        try:
            seq = request.query_param['seq']
            uid = request.query_param["uid"]
            text = request.query_param["text"]
            result = request.query_param["result"]

            if seq != None:
                seq = QuestionInput.objects.get(seq=seq)
                serializer = InputSerializer(seq)
            if uid != None:
                uid = QuestionInput.objects.get(uid=uid)
                serializer = InputSerializer(uid)
            if text != None:
                text = QuestionInput.objects.get(text=text)
                serializer = InputSerializer(text)
            if result != None:
                result = QuestionInput.objects.get(result=result)
                serializer = InputSerializer(result)
        except:
            quesinputs = self.get_queryset()
            serializer = InputSerializer(quesinputs, many=True)  # get all
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        input_data = request.data
        new_input = QuestionInput.objects.create(
            seq=genSeqID(input_data["uid"], input_data["index"]), uid=input_data["uid"], text=input_data["text"], result=input_data["result"])
        new_input.save()
        serializer = InputSerializer(new_input)
        return Response(serializer.data)
