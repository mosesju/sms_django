from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.texts, name='texts'),
    path('<str:pk>/', views.text_summary, name='text_summary')
]