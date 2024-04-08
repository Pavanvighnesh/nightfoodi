from django.shortcuts import render
from rest_framework import viewsets
from .models import movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset=movie.objects.all()
    serializer_class=MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
     queryset=movie.objects.filter(typ='action') 
     serializer_class=MovieSerializer   
class ComedyViewSet(viewsets.ModelViewSet):
     queryset=movie.objects.filter(typ='comedy') 
     serializer_class=MovieSerializer   
