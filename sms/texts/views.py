from django.shortcuts import render
from .models import *
# Create your views here.
def text(request):
    texts = Text.objects.all()
    context = {'texts':texts}
    return render(request, 'texts/texts.html', context)