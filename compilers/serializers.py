from rest_framework import serializers
from .models import Compiler


class CompilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compiler
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
        }
