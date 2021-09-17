from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate, login,logout  
from django.contrib.auth.models import User
from .forms import SignupForm,UserLoginForm

# Login page
def index(request): 
    login_form = UserLoginForm()
    context = {'form': login_form}
    return render(request,"/users/login",context)

# Registeration page
def register(request):
    if request.method == "POST":
        # sava new user to the database
        form  = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/users/login")
            
    else:
        # render registraion page
        form  = SignupForm(request.POST)
        context = {"form": form}
        return render(request, "registration/register.html",context)

