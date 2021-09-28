from django.urls import path,include
from .views import CreateRoomView, RoomView
urlpatterns = [
    path('home',RoomView.as_view()),
    path('create-room',CreateRoomView.as_view())
]