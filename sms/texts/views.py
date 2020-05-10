from django.shortcuts import render
from .models import *
# Create your views here.
def texts(request):
    texts = Text.objects.all()
    context = {'texts':texts}
    return render(request, 'texts/texts.html', context)

def text_summary(request, pk):
    text = Text.objects.get(id=pk)
    context = {'text':text}
    return render(request, 'texts/text_summary.html', context)