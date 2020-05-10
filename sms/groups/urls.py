from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.groups),
    path('<str:pk>/', views.group)
]