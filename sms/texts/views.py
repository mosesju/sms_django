from django.shortcuts import render, redirect
from .models import *
from .forms import TextForm
# Create your views here.
def texts(request):
    texts = Text.objects.all()
    context = {'texts':texts}
    return render(request, 'texts/texts.html', context)

def text_summary(request, pk):
    text = Text.objects.get(id=pk)
    context = {'text':text}
    return render(request, 'texts/text_summary.html', context)

def addText(request, pk):
    form = TextForm()
    if request.method =='POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'texts/text_form.html', context)

def addTextID(request, pk):
    group = Text.objects.get(id=pk)
    form = TextForm(initial={'group':group})
    if request.method =='POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'texts/text_form.html', context)

def updateText(request, pk):
    text = Text.objects.get(id=pk)
    form = TextForm(instance=text)

    if request.method =='POST':
        form = TextForm(request.POST, instance=text)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'texts/text_form.html', context)

def deleteText(request, pk):
    text = Text.objects.get(id=pk)
    if request.method == 'POST':
        text.delete()
        return redirect('/')
 
    context={'item':text}
    return render(request, 'texts/delete.html', context)