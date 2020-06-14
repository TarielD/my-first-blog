from rest_framework import serializers
from .models import Tag, Category, Post


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "title", "slug"]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "created_at", "updated_at", "body"]
