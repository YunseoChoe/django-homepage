from django.urls import path
from .views import UserCreateAPIView, LoginAPIView
from . import views

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]