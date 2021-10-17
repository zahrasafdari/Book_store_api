from django.db.models.base import Model
from rest_framework import serializers
from .models import Book

class BookSeriallizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    story_name = serializers.CharField(max_length=150)
    description = serializers.CharField()
    image = serializers.ImageField(default='' , use_url=True)
    fav = serializers.BooleanField(default=False)

class BookModelSeriallizer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'