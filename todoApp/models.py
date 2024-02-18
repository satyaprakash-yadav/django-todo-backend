from django.db import models

# Create your models here.

class Todo(models.Model):
    # create required todo fields 

    body = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    updated_At = models.DateTimeField(auto_now=True)
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
