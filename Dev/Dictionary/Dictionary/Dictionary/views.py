from django.http import HttpResponse
from django.shortcuts import redirect,render
from .forms import LoginForm,RegisterForm,DictionaryForm
from .Dictionary_module import find
from django.contrib.auth import login,authenticate,get_user_model
def home_page(request):
    context={
        "head":"Dictionary-Home",
        "title":"Dictionary",
        "content":"Click on login or register to start"
    }
    return render(request,"home.html",context)
def login_page(request):
    form=LoginForm(request.POST or None)
    context={
        "head":"Login",
        "content":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
    
        if user is not None:
            login(request,user)
            return redirect("/dictionary")
        else:
            print("Error")
    return render(request,"auth/login.html",context)
User=get_user_model()
def register_page(request):
    form=RegisterForm(request.POST or None)
    context={
        "head":"Register",
        "content":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        new_user=User.objects.create_user(username,email,password)
        if new_user is not None:
            return redirect("/login")
    return render(request,"auth/register.html",context)
def dictionary_page(request):
    form=DictionaryForm(request.POST or None )
    context={
        "head":"Find Meaning",
        "content":form
    }
    if form.is_valid():
        word=form.cleaned_data.get("word")
        print(find(word))
    return render(request,"dict.html",context)