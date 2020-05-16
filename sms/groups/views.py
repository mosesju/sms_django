from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from groups.models import *
from texts.models import Text
from .forms import GroupForm
from .filters import GroupFilter
# Create your views here.
@login_required(login_url='login')
def groups(request):
    # Filter by Account ID
    print(request)
    groups = Group.objects.all()
    # This should have a count for the total number of group members in the
    # template. Also I can build it so that there is management panel on top
    # where you can add a group, check the stats etc...
    # contacts = Contact.objects.
    myFilter = GroupFilter(request.GET, queryset=groups)
    groups = myFilter.qs
    context = {'groups': groups, 'myFilter': myFilter}
    return render(request, 'groups/groups.html', context)

@login_required(login_url='login')
def group(request, pk):
    group = Group.objects.get(id=pk)
    contact = Contact.objects.filter(group=group)
    # texts returns all texts belonging to the group
    texts = Text.objects.filter(group_id=pk)
    context = {'group':group, 'contact':contact,'texts':texts}
    return render(request, 'groups/group.html', context)

@login_required(login_url='login')
def addGroup(request):
    account = request.user
    form = GroupForm(instance=account)
    if request.method =='POST':
        form = GroupForm(request.POST, instance=account)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'groups/group_form.html', context)

@login_required(login_url='login')
def updateGroup(request, pk):
    group = Group.objects.get(id=pk)
    form = GroupForm(instance=group)

    if request.method =='POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'groups/group_form.html', context)

@login_required(login_url='login')
def deleteGroup(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('/')
 
    context={'item':group}
    return render(request, 'groups/delete.html', context)