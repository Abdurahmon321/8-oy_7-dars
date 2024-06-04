from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import FoodType, Food, Comment
from .serializers import FoodTypeSerializer, FoodSerializer, CommentSerializer


class FoodTypeViewSet(viewsets.ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer