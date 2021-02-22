from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout,authenticate
from .forms import TodoForms
from .models import Todo 
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'todoApp/home.html')

def signupuser(request):
    if request.method == 'GET':
        #this is used if method is get ... without logged inp person 
        return render(request, 'todoApp/signup.html',{'form': UserCreationForm()})
    else:
        #used for registering/signup of user 
        if request.POST['password1'] == request.POST['password2']:
            #password and confirm password must match 
            try:
                #block used for integrity exception handling
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodo')
            except IntegrityError:
                #if there is error of integrity then this block is used
                return render(request, 'todoApp/signup.html',{'form': UserCreationForm(),'error': 'user name is already present. Please choose another one '})
        else:
            #tell user that password does not matched
            return render(request, 'todoApp/signup.html',{'form': UserCreationForm(),'error': 'Password does not match '})
        
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request,'todoApp/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'todoApp/loginuser.html',{'form':AuthenticationForm(),'error': 'Please check the username and password'})
        else:
            login(request,user)
            return redirect('currenttodo')

@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request,'todoApp/createtodo.html',{'form':TodoForms()})        
    else:
        try:
            forms = TodoForms(request.POST)
            newtodo = forms.save(commit=False)
            newtodo.user = request.user
            print(newtodo.user)
            newtodo.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request,'todoApp/createtodo.html',{'form':TodoForms(),'error':'Please check the size of the title'})        

@login_required
def currenttodo(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request,'todoApp/currenttodo.html',{'todos':todos})

@login_required
def completedtodo(request):
    todo = Todo.objects.filter(user=request.user, date_completed__isnull=False)
    return render(request,'todoApp/completedtodo.html',{'todos':todo})

@login_required
def viewtodo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id,user= request.user)
    if request.method == 'GET':
        forms = TodoForms(instance=todo)
        return render(request,'todoApp/viewtodo.html',{'todo':todo,'form':forms})
    else:
        try:
            forms = TodoForms(request.POST, instance=todo)
            forms.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request,'todoApp/viewtodo.html',{'todo':todo,'form':forms,'error': 'bad data'})
@login_required
def completetodo(request,todo_id):
    todo = get_object_or_404(Todo,pk=todo_id,user = request.user)
    if request.method == 'POST':      
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('currenttodo')

@login_required
def deletetodo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id,user = request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodo')










