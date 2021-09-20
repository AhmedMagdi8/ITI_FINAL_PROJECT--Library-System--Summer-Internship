from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser  = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), initial=None)

    class Meta:
        model = User
        fields = ['username', 'is_superuser','first_name','last_name','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['is_superuser'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_superuser'].required = False
        self.fields['is_superuser'].default = False

        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        for user in User.objects.all():
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


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields ={'username':model.username,'password':forms.PasswordInput(),}


