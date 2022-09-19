from rest_framework import serializers
from .models import Player
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

class PlayerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Player
       fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'