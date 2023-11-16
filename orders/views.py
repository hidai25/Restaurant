from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import UserForm
from .models import Order, Product, Category
from django.contrib.auth.models import User
from cart.cart import Cart


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        # Use filter to divide the products in the categories
        "user": request.user,
        "Small_Regular_Pizza": Product.objects.filter(category=Category.objects.get(name='Small Regular Pizza')),
        "Large_Regular_Pizza": Product.objects.filter(category=Category.objects.get(name='Large Regular Pizza')),
        "Small_Sicilian_Pizza": Product.objects.filter(category=Category.objects.get(name='Small Sicilian Pizza')),
        "Large_Sicilian_Pizza": Product.objects.filter(category=Category.objects.get(name='Large Sicilian Pizza')),
        "Pizza_Toppings": Product.objects.filter(category=Category.objects.get(name='Pizza Toppings')),
        "Salad": Product.objects.filter(category=Category.objects.get(name='Salads')),
        "Pasta": Product.objects.filter(category=Category.objects.get(name='Pasta')),
        "Small_Subs": Product.objects.filter(category=Category.objects.get(name='Small Subs')),
        "Large_Subs": Product.objects.filter(category=Category.objects.get(name='Large Subs')),
        "Small_Dinner_Platter": Product.objects.filter(category=Category.objects.get(name='Small Dinner Platters')),
        "Large_Dinner_Platter": Product.objects.filter(category=Category.objects.get(name='Large Dinner Platters')),
    }
    return render(request, "orders/index.html", context)


def login_view(request):
    # Function used to login user
    if request.method == 'GET':
        return render(request, "orders/login.html")
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "invalid credentials"})


def logout_view(request):
    # Function used to logout user
    logout(request)
    return render(request, "orders/login.html", {"message": "logged out."})


def signup_view(request):
    # Function used to Register user with django forms. Taken from django documentation.
    if request.method == 'GET':
        form = UserForm()
        return render(request, "orders/signup.html", {'form': form})
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('repassword')
            user = authenticate(username=username, password=password1)
            #login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserForm()
    return render(request, 'orders/signup.html', {'form': form})
