from django.shortcuts import render

# Create your views here.
def text(request):
    return render(request, 'texts/texts.html')