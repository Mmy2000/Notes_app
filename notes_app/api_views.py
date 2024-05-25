from .models import Note
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import NotesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404

# class NotesListApi(generics.ListCreateAPIView):
#     serializer_class = NotesSerializer
#     queryset = Note.objects.all()
    # permission_classes = [IsAuthenticated,]

# class NotesDetailsApi(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = NotesSerializer
#     queryset = Note.objects.all()
    # permission_classes = [IsAuthenticated,]
@api_view(['GET'])
def post_list(request):
    all_post = Note.objects.all()
    data = NotesSerializer(all_post , many=True).data
    return Response({'data':data})

@api_view(['GET'])
def post_deatils_api(request , id):
    post = get_object_or_404(Note , id=id)
    data = NotesSerializer(post).data
    return Response({'data':data})