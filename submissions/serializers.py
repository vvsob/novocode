from rest_framework import serializers
from .models import Submission
from compilers.serializers import CompilerSerializer


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
        extra_kwargs = {
            'token': {'read_only': True},
        }


class SubmissionVerdictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
        extra_kwargs = {
            'token': {'read_only': True}
        }
