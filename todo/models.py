from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    tasktitle=models.CharField(max_length=50,default="")
    taskdesc=models.TextField(default="")
    date=models.CharField(max_length=50,default="")
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tasktitle
   
    
