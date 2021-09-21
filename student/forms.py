from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from users.models import CustomUser

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(max_length=300,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','image','bio','date_joined')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['email'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['image'].required = False
        self.fields['bio'].required = False
        self.fields['date_joined'].disabled = True
