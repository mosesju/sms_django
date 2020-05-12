from django.urls import path
from . import views

# Create your views here.
# Put pks at the bottom
urlpatterns = [
    path('', views.groups, name='groups'),
    path('add/', views.addGroup, name='add_group'),
    path('update/<str:pk>/', views.updateGroup, name='update_group'),
    path('delete/<str:pk>/', views.deleteGroup, name='delete_group'),
    path('<str:pk>/', views.group, name='group')
]