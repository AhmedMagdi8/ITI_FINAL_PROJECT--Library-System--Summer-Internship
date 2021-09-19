from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserChangeForm):
    # user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password1 = forms.PasswordInput(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password2 = forms.PasswordInput(widget=forms.TextInput(attrs={'class': 'form-control'}))

    # user_img =  forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined']

    def __init__(self, *args, **kwargs):
        super(UserChangeForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['email'].required = False
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['date_joined'].disabled = True