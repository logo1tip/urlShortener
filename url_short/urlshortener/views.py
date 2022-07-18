from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from .models import Shortener
from .forms import ShortenerForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import AbstractUser
from django.views.generic import ListView
from django.utils import timezone


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect("home")
        else:
            messages.error(request, "Registration error!")
    else:
        form = UserRegisterForm()
    return render(request,"urlshortener/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request,"urlshortener/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")


def home_view(request):
    template = 'urlshortener/home.html'
    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url 
            context['new_url']  = new_url
            context['long_url'] = long_url
            
            return render(request, template, context)

        context['errors'] = used_form.errors
        return render(request, template, context)


def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1        
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        raise Http404('Sorry this link is broken :(')
 

def all_urls(request):
    
    if request.user.is_authenticated:
        logged_in_owner = request.user
        urls_list = Shortener.objects.all()
        return render(request, "urlshortener/all_urls.html", {"urls_list": urls_list})
    else:
        return render(request, "urlshortener/home.html", {})    

