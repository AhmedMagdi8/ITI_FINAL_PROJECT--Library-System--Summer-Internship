from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=200,null=True)
    authors = models.CharField(max_length=200,null=True)
    image = models.ImageField(max_length=200,null=True)
    description = models.TextField(null=True, blank=True)
    is_borrowed = models.BooleanField(null=True)
    std_id = models.ForeignKey(User,on_delete=models.CASCADE,default=1000)