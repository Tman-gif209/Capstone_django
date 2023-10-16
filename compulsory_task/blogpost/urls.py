from django.views.generic import DetailView, ListView
from django.urls import path
from .models import Post
from django.conf import settings
from django.conf.urls.static import static
#from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from blogpost import views as user_views
from blogpost import views
#from django.views.generic import RedirectView

urlpatterns = [
    path('',
        ListView.as_view(
            model=Post,
            template_name="post.html"
           )
        ),
    path('home.html',
        ListView.as_view(
            model = Post,
            template_name="home.html"
           )
        ),
    path('blogpost.html',
        ListView.as_view(
            model = Post,
            template_name="blogpost.html"
            )
        ),   
    path('post.html',
        ListView.as_view(queryset=
        Post.objects.all().order_by("-date")[:25],
        template_name="post.html"
            )
        ),
    path('membership.html',
        ListView.as_view(
            model = Post,
            template_name="membership.html"
            )
        ),
    path('paymentsite.html',
        ListView.as_view(
            model = Post,
            template_name="paymentsite.html"
            )
        ),
    path('register.html',
        ListView.as_view(
            model = Post,
            template_name="register.html"
            )
        ),
    path('login.html',
        auth_views.LogoutView.as_view(
            template_name="login.html"
            ), name='logout'
        ),
    path('logout.html',
        views.logout_user,name='logout'
        ),
]+ static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)