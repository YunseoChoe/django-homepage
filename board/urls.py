from django.urls import path
from .views import BoardCreateAPIView

urlpatterns = [
    path('boardcreate/', BoardCreateAPIView.as_view()),
]