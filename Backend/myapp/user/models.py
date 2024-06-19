from django.db import models

# Create your models here.
class asthamauser(models.Model):
    username=models.CharField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
    age=models.CharField(max_length=50,null=True,blank=True)
    gender=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=255,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.username
    
    