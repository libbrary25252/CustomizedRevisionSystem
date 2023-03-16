from rest_framework import serializers
from .models import User, Question, QuestionQuestion

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['QID', 'parentQID', 'statement', 'string', 'Qtype', 'image', 
                  'description', 'options', 'category']

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionQuestion
        field = ['state_id', 'statement', 'qid']