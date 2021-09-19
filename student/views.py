from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from adminn.models import Book
from .forms import EditProfileForm

# Create your views here.

def Dashboard(request):
    books = Book.objects.all()
    lst = []
    for book in books:
        lst.append(book)
        print(book.id)

    lst.sort(key=lambda x: x.id)
    context = {"books": lst}
    return render(request, "student/Dashboard.html",context=context)


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "student/EditProfile.html"
    success_url = reverse_lazy("dashboard")

    def get_object(self):
        return self.request.user


def show(request):
    if request.method =="GET":  
        students = User.objects.all()
        context = {"students": students}
        return render(request, "student/showstudents.html",context=context)
    if request.method =="POST":  
        idd = int(request.POST["searchid"])
        student = [student for student in list(User.objects.all()) if student.id== idd and student.is_superuser == False ]
        context = {"students": student}
        return render(request, "student/showstudents.html",context=context)


def mybooks(request,user_id):
    books = [book for book in list(Book.objects.all()) if book.is_borrowed and book.std_id.id == user_id] 
    context = {"books":books}
    return render(request, "student/mybooks.html",context=context)


def showborrowedstd(request):
    books = [book for book in list(Book.objects.all()) if book.is_borrowed == True ]
    context = {"books": books}
    return render(request, "student/borrowedbooks.html",context=context)


def booknow(request, book_id, user_id):
    # book = get_object_or_404(Book, pk=book_id)
    user = User.objects.filter(pk=user_id)[0]
    Book.objects.filter(pk=book_id).update(
        is_borrowed=True,
        std_id=user,
        return_date= request.POST["return_date"]
        )
    print('book id',book_id,'user id' , user_id,'hellllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllo')
    return redirect("dashboard")

def return_book(request, book_id, user_id):
    # book = get_object_or_404(Book, pk=book_id)
    user = User.objects.filter(pk=user_id)[0]
    Book.objects.filter(pk=book_id).update(
        is_borrowed=False,
        std_id=None,
        return_date= None
        )
    return redirect("dashboard")


