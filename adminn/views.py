from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Book
from .forms import BookModelForm
# Create your views here.

def Dashboard(request):
    books = Book.objects.all()
    lst = []
    for book in books:
        lst.append(book)

    lst.sort(key=lambda x: x.id)
    context = {"books": lst}
    return render(request, "adminn/Dashboard.html",context=context)


def show(request):
    if request.method =="GET":  
        students = User.objects.all()
        lst = []
        for std in students:
            if not std.is_superuser:
                lst.append(std)
        context = {"students": lst}
        return render(request, "adminn/showstudents.html",context=context)
    # search student
    if request.method =="POST":  
        idd = int(request.POST["searchid"])
        student = [student for student in list(User.objects.all()) if student.id== idd and student.is_superuser == False ]
        context = {"students": student}
        for student in list(User.objects.all()):
            print(student.id,student.id == idd)
        return render(request, "adminn/showstudents.html",context=context)

def showstudent(request,student_id):
    student = [student for student in list(User.objects.all()) if student.id== student_id]
    context = {"student": student[0]}
    return render(request, "adminn/student.html",context=context)


def showborrowed(request):
    books = [book for book in list(Book.objects.all()) if book.is_borrowed == True ]
    context = {"books": books}
    return render(request, "adminn/borrowedbooks.html",context=context)


def editbook(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method =="GET":  
        context={"book": book}
        return render(request, "adminn/editbook.html", context)
    if request.method =='POST':
        Book.objects.filter(pk=book_id).update(
            name=request.POST["name"],
            authors=request.POST["authors"],
            image=request.POST["img"],
            description=request.POST["description"])
        return redirect("Dashboard")



def deletebook(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect("Dashboard")


def add(request):
    form = BookModelForm()
    if request.method == "GET":
        context = {"form": form}
        return render(request, "adminn/addbook.html",context)

    if request.method =="POST":
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save() 
        else:
            print(form.errors)
        return redirect("Dashboard")



def changepass(request,user_id):
    if request.method =="GET":  
        return render(request, "adminn/changepass.html")
    if request.method =="POST":
        new_password = request.POST["password"]
        admin = User.objects.get(id=user_id)
        admin.set_password(new_password)
        admin.save()
    return redirect("logout")

