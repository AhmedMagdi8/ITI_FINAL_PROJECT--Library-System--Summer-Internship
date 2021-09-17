from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


# Create your views here.

def Dashboard(request):
    return render(request, "books/Dashboard.html")


class UserEditView(generic.UpdateView):
    # print('hi')
    form_class = UserChangeForm
    template_name = "books/EditProfile.html"
    success_url = reverse_lazy("Dashboard")

    def get_object(self):
        return self.request.user


def show(request):
    students = User.objects.all()
    context = {"students": students}
    return render(request, "books/showstudents.html",context=context)

def add(request):
    students = User.objects.all()
    context = {"students": students}
    return render(request, "books/showstudents.html",context=context)

def search(request):
    students = User.objects.all()
    context = {"students": students}
    return render(request, "books/showstudents.html",context=context)

def mybooks (request):
    students = User.objects.all()
    context = {"students": students}
    return render(request, "books/showstudents.html",context=context)

def changepass(request):
    students = User.objects.all()
    context = {"students": students}
    return render(request, "books/showstudents.html",context=context)

def logout(request):
    logout()
