from adminn.models import Book
from django.db import models
from django import forms




class BookModelForm(forms.ModelForm):
    # create from according the model , just specify fields
    class Meta:
        model = Book
        fields = ["name", "authors", "description", "image","is_borrowed","std_id"]


