from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]