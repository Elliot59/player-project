from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'player', views.PlayerView)
router.register(r'signup', views.PlayerSignUpView)
router.register(r'login', views.LoginSerializerView)

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', views.Logout),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]