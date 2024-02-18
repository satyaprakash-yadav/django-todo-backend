from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .models import Todo

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer

