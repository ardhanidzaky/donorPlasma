from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/home/login')
def tryLogin(request):
    return render(request, 'tryLogin.html')

def register_request(request):
    form = NewUserForm()
    if request.is_ajax():
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg': 'Success',
            })
        else:
            return JsonResponse({
                'msg': 'Failed',
            })
        

    context = {
        'register_form': form
    }
    return render(request, 'reg.html', context)

def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
                
    context = {
        'login_form': form
    }

    return render(request, 'login.html', context)

@login_required(login_url='/home/login')
def logout_request(request):
    return render(logout(request), 'logout.html')
    # Redirect to a success page.

@login_required(login_url='/home/login')
def daftar(request):
    return render(request, 'choices.html')
