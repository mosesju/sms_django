from django.urls import path
from . import views

# Create your views here.
# Put pks at the bottom
urlpatterns = [
    path('', views.groups, name='groups'),
    path('add/', views.addGroup, name='addGroup'),
    path('<str:pk>/', views.group, name='group')
]