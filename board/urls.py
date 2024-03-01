from django.urls import path
from .views import BoardCreateAPIView
from .views import BoardUpdateAPIView
from .views import BoardDeleteAPIView
from .views import BoardReadAPIView
from .views import BoardAllReadApi
from .views import CommentAPI

urlpatterns = [
    path('board_create/', BoardCreateAPIView.as_view()),
    path('board_update/<int:pk>/', BoardUpdateAPIView.as_view()),
    path('board_delete/<int:pk>/', BoardDeleteAPIView.as_view()),
    path('board_read/<int:pk>/', BoardReadAPIView.as_view()),
    path('board_all_read/', BoardAllReadApi.as_view()),
    path('board_comment/<int:pk>/', CommentAPI.as_view()),
]