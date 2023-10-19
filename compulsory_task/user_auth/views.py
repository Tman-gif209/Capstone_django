from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def user_login(request):
    """
    Once user enters login in details, python program checks if there is a user with that name and password.
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Python program to make sure the username and password from user is valid,if not user will have to login again until information entered is correct but if login details are valid/correct the user will be directed to another page.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
    
def show_user(request):
    """
    Python program to display the usernme and password of th user.
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
