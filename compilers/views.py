from .models import Compiler
from .serializers import CompilerSerializer
from rest_framework import generics, mixins, status


class CompilerList(generics.ListCreateAPIView):
    queryset = Compiler.objects.all()
    serializer_class = CompilerSerializer


class CompilerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compiler.objects.all()
    serializer_class = CompilerSerializer
