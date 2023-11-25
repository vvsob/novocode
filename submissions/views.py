import uuid

from .models import Submission
from .serializers import SubmissionSerializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response


class SubmissionList(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def post(self, request, *args, **kwargs):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['token'] = str(uuid.uuid4())
            serializer.save()
            return Response({'token': serializer.data['token']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
