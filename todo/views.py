from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from todo.models import Task
import json
# Create your views here.
def index(request):
    context={"success":False}

    if request.method=="POST":
        # print(request.POST)
        title=request.POST['title']
        desc=request.POST['desc']
        dat=request.POST['date']
        ins=Task(tasktitle=title,taskdesc=desc,date=dat)
        ins.save()
        context={"success":True}
        # print(title,desc)

    return render(request,'index.html',context)

def task(request):
    alltasks=Task.objects.all() 
    return render(request,'task.html',{"alltasks":alltasks})


def delete_todo(request,todo_id):
    instance = get_object_or_404(Task,id=todo_id)
    instance.delete()
    return task(request)
def delete_all(request):
    alltasks=Task.objects.all()
    alltasks.delete()
    return task(request)

def update_task(request, pk):
    context={"success":False}
    if request.method=="POST":
        Task.objects.filter(id=pk).update(tasktitle=request.POST['title'],taskdesc=request.POST['desc'],date=request.POST['date'])
        # task.refresh_from_db()
        context={"success":True}
        return task(request)
    return render(request, "update_task.html",context)
    

