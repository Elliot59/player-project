from rest_framework import serializers
from .models import Player
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

class PlayerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Player
       fields = '__all__'

