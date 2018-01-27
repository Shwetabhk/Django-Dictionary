from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()
class DictionaryForm(forms.Form):
    word=forms.CharField(label="Enter the word",widget=forms.TextInput(attrs={"placeholder":"Enter the word","class":"form-control"}))
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter Password"}))
class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter Username"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Enter E-mail"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter Password"}))
    conpassword=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already exists")
        return username
    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("E-mail already exists")
        return email
    def clean_pass(self):
        data=self.cleaned_data
        pass1=self.cleaned_data("password")
        pass2=self.cleaned_data("conpassword")
        if password!=conpassword:
            raise forms.ValidationError("Passwords do not match")
        return data