from .models import Problem
from .serializers import ProblemSerializer, ProblemListSerializer
from rest_framework import generics, mixins, status


class ProblemList(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer


class ProblemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
