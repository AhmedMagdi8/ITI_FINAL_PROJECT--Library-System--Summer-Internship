from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate, login,logout  
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages
# Login page
def index(request):
    if request.method == 'GET':
        return render(request, "registration/login.html")

    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( request,username = username, password = password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return HttpResponseRedirect("/adminn/dashboard")
            else:
                login(request, user)
                return HttpResponseRedirect(f"/student/mybooks/{user.id}")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('index')


# Registeration page

def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/users/login")

    context = {"form": form}
    return render(request, "registration/register.html",context)

