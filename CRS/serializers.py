from rest_framework import serializers
from .models import User, Question, QuestionQuestion, QuestionInput


class QuestionSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        children = obj.question_set.all()
        if children:
            serializer = self.__class__(children, many=True)
            return serializer.data
        return None

    class Meta:
        model = Question
        fields = ['QID', 'parentQID', 'statement', 'string', 'Qtype', 'image',
                  'description', 'options', 'category', 'children']


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionQuestion
        fields = ['state_id', 'statement', 'qid']


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionInput
        fields = ['seq', 'uid', 'text', 'result']

