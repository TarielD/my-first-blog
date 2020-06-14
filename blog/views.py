from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Category, Tag, Post
from .serializers import TagSerializers, CategorySerializers, PostSerializers


class TagListApiView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class TagDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class CategoryListApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
