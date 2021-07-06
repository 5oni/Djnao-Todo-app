from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from todo.models import Task
import json

# Create your views here.
def index(request):
    context={"success":False}
    
    if not request.user.is_authenticated:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
            else:
                user= User.objects.create_user(username=username,password=password)
                user.save()
                login(request,user)
            return redirect("/")
        return render(request,'login.html',context)
    if request.method=="POST":
        
        title=request.POST['title']
        desc=request.POST['desc']
        dat=request.POST['date']
        ins=Task(username=request.user,tasktitle=title,taskdesc=desc,date=dat)
        ins.save()
        context={"success":True}
        # print(title,desc)

    return render(request,'index.html',context)

def task(request):
    alltasks=Task.objects.filter(username=request.user) 
    return render(request,'task.html',{"alltasks":alltasks})


def delete_todo(request,todo_id):
    instance = get_object_or_404(Task,id=todo_id)
    instance.delete()
    return redirect('/task/')
def delete_all(request):
    alltasks=Task.objects.all()
    alltasks.delete()
    return task(request)

def update_task(request, pk):
    context={"success":False}
    if request.method=="POST":
        alltasks=Task.objects.all() 
        Task.objects.filter(id=pk).update(tasktitle=request.POST['title'],taskdesc=request.POST['desc'],date=request.POST['date'])
        # task.refresh_from_db()
        context={"success":True,"alltasks":alltasks}
        # return task(request)
        return render(request, "task.html",context)
        
    return render(request, "update_task.html",context)
    

def LogoutView(request):
    logout(request)
    return redirect("/")
