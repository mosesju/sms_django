from django.forms import ModelForm
from .models import *

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'