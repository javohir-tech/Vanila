from django import forms
from django.contrib.auth.models import User


class LoginForms(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="parol")

    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="parolni qayta yozish"
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and password != confirm_password:
            raise forms.ValidationError("Password not match")
        return cleaned_data
