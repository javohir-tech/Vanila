from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForms(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class UserRegisterCloneForm(forms.ModelForm):
    # pass
    password = forms.CharField(widget=forms.PasswordInput, label="parol")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="qayta parol")

    class Meta :
        model = User
        fields = ['username','email' , 'first_name']
        
    def clean(self) :
        data = super().clean()
        password1 = data.get('password')
        password2 = data.get('confirm_password')
        
        if password1  and password1 != password2 :
            raise   forms.ValidationError('Password not match')
        
        return data