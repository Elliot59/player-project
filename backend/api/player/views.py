from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from api.player.models import Player
from django.contrib.auth.models import User, auth
from django.contrib.auth import  get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PlayerSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.decorators import method_decorator
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token


class PlayerView(viewsets.ModelViewSet):
        queryset = Player.objects.all()
        serializer_class = PlayerSerializer
        def list(self, request, *args, **kwargs):
            return Response(PlayerSerializer(Player.objects.all(), many=True).data)


class PlayerSignUpView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def list(self, request, *args, **kwargs):
        return Response({'get_method_status': False})
    @csrf_exempt
    def create(self, request, *args, **kwargs):
        get_data = request.data
        new_player = Player(user=get_user_model().objects.create_user(username=get_data['name'],password=get_data['password']),
                                                                            name=get_data['name'],
                                                                            age=get_data['age'],
                                                                            height=get_data['height'],
                                                                            email=get_data['email'],
                                                                            password=get_data['password'],
                                                                            confirm_password=get_data['confirm_password']
                                          )
        token, _ = Token.objects.get_or_create(user=User.objects.get(username=get_data['name']))
        if token:
            new_player.save()
        elif token == '':
            new_player.save(commit=False)

        serializer = PlayerSerializer(new_player)
        return Response(serializer.data)


class LoginSerializerView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    @csrf_exempt
    def list(self, request, *args, **kwargs):
        return Response({'get_method_status': False})

    @csrf_exempt
    def create(self, request, *args, **kwargs):

        get_data = request.data
        if request.method == "GET":
            if request.user.is_authenticated:
                return HttpResponse('You are already logged in')
            else:
                return HttpResponse('GET request not allowed')
        else:
            try:
                username = get_data['name']
                password = get_data['password']
                user = User.objects.get(username=username)
                if user is not None:
                    if authenticate(request, username=username, password=password):
                        try:
                            if Token.objects.get(user=user):
                                login(request, user)
                        except ObjectDoesNotExist:
                            return HttpResponse({'Token error'})
                        a = Player.objects.filter(name=username).values_list('is_captain', flat=True).first()
                        try:
                            if a == True:
                                return HttpResponse('Welcome captain')
                            else:
                                return HttpResponse(f'Logged in as {user}')
                        except ObjectDoesNotExist:
                            return HttpResponse(f'Logged in as admin {user}')
                    else:
                        return HttpResponse('Not Authenticated')
                else:
                    return HttpResponse('User not found')
            except ObjectDoesNotExist:
                return HttpResponse('Object not found')

@csrf_exempt
def Logout(request):
    logout(request)
    return HttpResponse('Logged out successful')

