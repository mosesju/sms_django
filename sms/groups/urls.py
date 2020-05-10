from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.groups, name='groups'),
    path('<str:pk>/', views.group, name='group')
]