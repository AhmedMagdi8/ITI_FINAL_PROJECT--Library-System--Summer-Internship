from books.models import Book
from django.db import models
from django import forms


# class BookForm(forms.Form):
#     name = forms.CharField(label="Book name", min_length=5)
#     authors = forms.CharField(label="Book authors")
#     image = forms.ImageField(label="Book image")
#     description = forms.CharField(label="Book description")
#     is_borrowed = forms.BooleanField(label="Book is borrowed")
#     std_id = forms.CharField(label="Student ID")


class BookModelForm(forms.ModelForm):
    # create from according the model , just specify fields
    class Meta:
        model = Book
        fields = ["name", "authors", "description", "image","is_borrowed","std_id"]


# class BookEditForm(forms.UpdateView):
#     class Meta:
#         model = Book
#         fields = ["name", "authors", "description", "image","is_borrowed","std_id"]

