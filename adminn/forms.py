from adminn.models import Book
from django.db import models
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from users.models import CustomUser




class BookModelForm(forms.ModelForm):
    # create from according the model , just specify fields
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control mb-3 mp-3'}))
    authors = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control mb-3 mp-3'}))
    description = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control mb-3 mp-3'}))
    image = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control mb-3 mp-3'}))
    class Meta:
        model = Book
        fields = ["name", "authors", "description", "image"]




