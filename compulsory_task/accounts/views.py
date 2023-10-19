from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView):
    """
    Python program to set a up Signup page for users to make a account.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

