from multiprocessing.sharedctypes import Value
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny

from django.contrib.auth.models import User
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
    return render(logout(request), 'home.html')
    # Redirect to a success page.

@login_required(login_url='/home/login')
def daftar(request):
    return render(request, 'choices.html')

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [AllowAny]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )