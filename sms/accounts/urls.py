from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('account/', views.account, name='account')
]