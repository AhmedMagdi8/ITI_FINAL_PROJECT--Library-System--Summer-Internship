from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate, login,logout  
from django.contrib.auth.models import User
from .forms import SignupForm,UserLoginForm

# Login page
def index(request): 
    # login_form = UserLoginForm()
    # context = {'form': login_form}
    return render(request, "registration/login.html")


def handle_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate( request,username = username, password = password)
    if user is not None:
        if user.is_superuser:
            login(request, user)
            print("first")
            return HttpResponseRedirect("/adminn/dashboard")
        else:
            login(request, user)
            print('second',user.id)
            return HttpResponseRedirect(f"/adminn/mybooks/{user.id}")
    
    print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
# Registeration page
def register(request):
    if request.method == "POST":
        # sava new user to the database
        form  = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/users/login")
        else:
            if form.errors:
                form  = SignupForm()
                context = {"form": form}
                return render(request, "registration/register.html",context)

    else:
        # render registraion page
        form  = SignupForm()
        context = {"form": form}
        return render(request, "registration/register.html",context)



