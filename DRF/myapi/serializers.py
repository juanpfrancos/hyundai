#Import the REST Framework serializer
# #Import the Hero model
from rest_framework import serializers
from .models import Hero

#Create a new class that links the Hero with its serializer

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'alias')