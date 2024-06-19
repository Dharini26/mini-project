from django.db import models

# Create your models here.

class asthamaadmin(models.Model):
    username=models.CharField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.username
    