from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, AccountForm
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
def accountSettings(request):
    # request.user is the username
    account = request.user.account
    form = AccountForm(instance=account)
    if request == 'POST':
        form = AccountForm(request.POST, request.FILES , instance=account)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'accounts/account.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            account = Account.objects.create(
                user=user,
                name=user.username,
                email=email
            )
            print(account)
            messages.success(request, 'Account was created for '+username)
            return redirect('login')
        else:
            messages.info(request, 'Something went wrong')

    context={'form':form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
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