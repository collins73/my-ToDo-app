from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ToDoListForm
from django.contrib import messages



from django.http import HttpResponseRedirect


def home(request):

    if request.method == 'POST':
        form = ToDoListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = ToDoList.objects.all()
            messages.success(request, ('New Item Added To The List'))
            return render(request, 'home.html', {'all_items':all_items})
    else:

        all_items = ToDoList.objects.all()
        return render(request, 'home.html', {'all_items':all_items})

def about(request):
    context = {'name':'Demayne Collins'}
    return render(request, 'about.html', context)


def delete(request, list_id):
        item = ToDoList.objects.get(pk=list_id)
        item.delete() 
        messages.success(request, ('Item Successfully Deleted from The To Do List!'))
        return redirect('home')


def cross_off(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = ToDoList.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = ToDoList.objects.get(pk=list_id)
        form = ToDoListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Update was Successful!'))
            return redirect('home')
    else:

        item = ToDoList.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item':item})
    
    
