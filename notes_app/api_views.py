from .models import Note
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import NotesSerializer

class NotesListApi(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated,]

class NotesDetailsApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotesSerializer
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated,]