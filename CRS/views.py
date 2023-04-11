from .serializers import QuestionSerializer, ContainerSerializer, InputSerializer, UserSerializer, UserInfoSerializer
import datetime
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, QuestionQuestion, QuestionInput, User, UserInfo
from django.conf import settings
from django.http import Http404, JsonResponse
from rest_framework import permissions, authentication
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


def home(request):
    return render(request, 'home.html', {'name': 'Hello'})


def get_image(request, pk):
    my_model = Question.objects.get(QID=pk)
    image_path = os.path.join(settings.MEDIA_URL, str(my_model.image))
    return JsonResponse({'image_path': image_path})


def genSeqID(uid, sequence):
    time = datetime.datetime.now()
    str_time = str(time).replace("-", "").replace(" ", "").replace(":", "")
    str_time = str_time[:str_time.rfind('.')]
    res = uid + "-" + str_time + "-" + str(sequence)
    print(res)
    return res


class UserAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all()
        return user

    def post(self, request, *args, **kwargs):
        data = request.data
        token = data['token']
        print('\nposted data: ' + token)
        token_obj = Token.objects.get(key=token)
        # Access the user object from the token object
        user = token_obj.user
        users = User.objects.get(user=user)
        serializer = UserSerializer(users, many=False)
        # try:

        # except:
        #     users = self.get_queryset()
        #     serializer = UserSerializer(users, many=True)  # get all
        return Response(serializer.data)


class QuestionAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        questions = Question.objects.all()
        return questions

    def get(self, request, *args, **kwargs):
        try:
            # ID = request.query_param["QID"]
            # parentID = request.query_param["parentQID"]
            # statement = request.query_param["statement"]
            # string = request.query_param["string"]
            # imagefile = request.query_param["image"]
            # description = request.query_param["description"]
            # option = request.query_param["option"]
            # type = request.query_params.getlist('Qtype')
            # topics = request.query_params.getlist('category')
            # type = request.query_param["Qtype"]
            # topics = request.query_param["category"]
            # print(type, topics)

            # if type is not None and topics is not None:
            #     questions = Question.objects.filter(
            #         Qtype__in=type, category__in=topics)
            # elif type is not None:
            #     questions = Question.objects.filter(Qtype__in=type)
            # elif topics is not None:
            #     questions = Question.objects.filter(category__in=topics)

            # parentID = ''

            # if parentID is not None:
            #     parent_question = Question.objects.get(QID=parentID)
            #     child_questions = parent_question.child_questions.all()
            #     serializer = QuestionSerializer(child_questions, many=True)
            #     return Response(serializer.data)
            # else:
            questions = self.get_queryset()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        except Question.DoesNotExist:
            raise Http404

    def post(self, request, *args, **kwargs):
        question_data = request.data
        new_question = Question.objects.create(QID=question_data["QID"], statement=question_data["statement"], string=question_data["string"],
                                               Qtype=question_data["Qtype"], description=question_data["description"], options=question_data["options"], image=question_data["image"], category=question_data["category"])
        new_question.save()
        serializer = QuestionSerializer(new_question)
        return Response(serializer.data)


class ContainerAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
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
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
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
