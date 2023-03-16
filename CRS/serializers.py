from rest_framework import serializers
from .models import User, Question, QuestionQuestion, QuestionInput
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['QID', 'parentQID', 'statement', 'string', 'Qtype', 'image', 
                  'description', 'options', 'category']

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionQuestion
        fields = ['state_id', 'statement', 'qid']

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionInput
        fields = ['uid', 'text', 'result']