from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import CustomUser
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200)
    authors = models.CharField(max_length=200,blank=True)
    image = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    is_borrowed = models.BooleanField(blank=True,default=False)
    std_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)
    return_date = models.DateField(blank=True,null=True)

