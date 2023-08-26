from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import Task
from .forms import *
def index(request):
    #return HttpResponse('heelo world')
    task=Task.objects.all()
    form=FormTask()
    if request.method=='POST':
        form=FormTask(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
      
    context={'task': task,'form':form}
    return render(request,'tasks/list.html',context)


def updateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=FormTask(instance=task)
    if request.method=='POST':
        form=FormTask(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return  redirect('/')  
    context={'form':form}     
    return render(request,'tasks/update_task.html',context)
def delet(request,pk):
    item=Task.objects.get(id=pk)
   
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context={'item':item}    
    return render(request,'tasks/delete_task.html',context)
    
    

