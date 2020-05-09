from django.shortcuts import render
from groups.models import *
from texts.models import *
# Create your views here.
def home(request):
    groups = Group.objects.all()
    texts = Text.objects.all()
    context = {'groups':groups, 'texts':texts}
    return render(request, 'accounts/dashboard.html', context)
