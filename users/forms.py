from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
    )
    is_superuser = forms.ChoiceField(choices = TRUE_FALSE_CHOICES)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username' ,'is_superuser','first_name','email','password1','password2',)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['is_superuser'].widget.attrs['class'] = 'form-control'
        self.fields['is_superuser'].required = True
        self.fields['is_superuser'].default = False
        self.fields['first_name'].required = True
        self.fields['email'].required = True


        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_username(self):
        username = self.cleaned_data.get("username")
        for user in CustomUser.objects.all():
            if user.username == username:
                raise forms.ValidationError("User already exists")
            else:
                return username

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        SpecialSym =['$', '@', '#','%']
        if len(password1) < 8:
            raise forms.ValidationError("password must be at least 8 characters")
        elif not any(char in SpecialSym for char in password1):
            raise forms.ValidationError("password must be at least 8 characters and contains complex characters $,%,@,# or not be too common")
        else:
            return password1


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password2 != password1:
            raise forms.ValidationError("password not match")
        else:
            return password2


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username' ,'is_superuser','first_name', 'last_name','email',)

