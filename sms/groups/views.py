from django.shortcuts import render
from groups.models import *
from texts.models import Text
# Create your views here.
def groups(request):
    # Filter by Account ID
    groups = Group.objects.all()
    # This should have a count for the total number of group members
    # contacts = Contact.objects.
    context = {'groups': groups}
    return render(request, 'groups/groups.html', context)
def group(request, pk):
    group = Group.objects.get(id=pk)
    contact = Contact.objects.filter(group=group)
    # texts returns all texts belonging to the group
    texts = Text.objects.filter(group_id=pk)
    context = {'group':group, 'contact':contact,'texts':texts}
    return render(request, 'groups/group.html', context)