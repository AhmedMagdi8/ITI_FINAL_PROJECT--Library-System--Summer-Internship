from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser  = forms.BooleanField(widget=forms.CheckboxInput, initial=None)
    # user_img =  forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'is_superuser','first_name','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['is_superuser'].required = False
        self.fields['is_superuser'].default = False
        # self.fields['user_img'].required = True

        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None
            
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields ={'username':model.username,'password':forms.PasswordInput(),}


