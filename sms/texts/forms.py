from django.forms import ModelForm
from .models import *

class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = '__all__'