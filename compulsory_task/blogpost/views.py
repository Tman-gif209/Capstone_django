from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm as UserRegistrationForm
#from django.contrib.auth.decorators import login_required

# Create your views here.


def post(request, *args, **kwargs):
    """
    Python program to display the post webpage
    """
    return render(request, "post.html")

def blogpost(req):
    """
    Python program to display the blogpost webpage
    """
    return render(req, "blogpost.html")

def payment(req):
    """
    Python program to display the payment webpage
    """
    return render(req,"paymentsite.html")

def member(req):
    """
    Python program to display the membership webpage
    """
    return render(req, "membership.html")

def home(req):
    """
    Python program to display the home webpage
    """
    return render(req, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!') 
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'blogpost/register.html', context)

def logout_user(req):
    """
    Python program to display the logout webpage
    """
    return render(req, 'logout.html')