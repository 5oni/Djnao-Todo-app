from django.db import models

# Create your models here.
class Task(models.Model):
    tasktitle=models.CharField(max_length=50)
    taskdesc=models.TextField()
    date=models.CharField(max_length=50)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tasktitle
    
