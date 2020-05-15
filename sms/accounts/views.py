from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from groups.models import *
from texts.models import *
from .models import *
from .decorators import unauthenticated_user
# Create your views here.
@login_required(login_url='login')
def home(request):
    groups = Group.objects.all()
    texts = Text.objects.all()
    context = {'groups':groups, 'texts':texts}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def account(request):
    # accounts=
    context={}
    return render(request, 'accounts/account.html', context)

@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+user)
                return redirect('login')
        context={'form':form}
        return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username OR password is incorrect')
        context={}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')