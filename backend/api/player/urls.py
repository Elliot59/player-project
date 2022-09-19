from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.PlayerView, basename='player')
router.register(r'signup', views.PlayerSignUpView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.Login),
    path('logout/', views.Logout),


]