from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=200,blank=True,null=True)
    is_superuser = models.BooleanField(default=False,null=True)
    date_joined = models.DateField(null=True,default=timezone.now)
    image = models.CharField(max_length=200,blank=True,null=True)
    bio = models.TextField(max_length=300,blank=True,null=True)