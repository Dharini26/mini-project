from django.db import models
from datetime import datetime

# Create your models here.
class inhaler(models.Model):
     username=models.CharField(max_length=50,null=True,blank=True)
     date=models.DateTimeField(default=datetime.now)
     
     def __str__(self):
        return self.username