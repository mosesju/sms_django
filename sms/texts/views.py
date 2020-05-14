from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import TextForm
from .filters import TextFilter
# Create your views here.
@login_required(login_url='login')
def texts(request):
    texts = Text.objects.all()
    context = {'texts':texts}
    return render(request, 'texts/texts.html', context)

@login_required(login_url='login')
def text_summary(request, pk):
    text = Text.objects.get(id=pk)
    context = {'text':text}
    return render(request, 'texts/text_summary.html', context)

@login_required(login_url='login')
def addText(request, pk):
    form = TextForm()
    if request.method =='POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'texts/text_form.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteText(request, pk):
    text = Text.objects.get(id=pk)
    if request.method == 'POST':
        text.delete()
        return redirect('/')
 
    context={'item':text}
    return render(request, 'texts/delete.html', context)