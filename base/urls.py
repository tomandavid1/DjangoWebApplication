from django.urls import path
from . import views

# Base url patterns
urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
]