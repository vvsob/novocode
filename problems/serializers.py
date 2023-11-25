from rest_framework import serializers
from .models import Problem
from submissions.serializers import SubmissionSerializer


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['id', 'name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
        }
