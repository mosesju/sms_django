from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.texts, name='texts'),
    path('add/', views.addText, name='add_text'),
    path('add/<str:pk>/', views.addTextID, name='add_text_id'),
    path('update/<str:pk>/', views.updateText, name='update_text'),
    path('delete/<str:pk>/', views.deleteText, name='delete_text'),
    path('<str:pk>/', views.text_summary, name='text_summary')
]