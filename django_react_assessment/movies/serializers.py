from rest_framework import serializers
from .models import Movie

# Lead Serializer
class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = '__all__'