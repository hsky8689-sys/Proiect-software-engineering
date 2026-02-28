from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import User


# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        birthday = request.POST['birthday']

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),  # HASH CRUCIAL!
            birthday=birthday
        )
        messages.success(request, 'Cont creat!')
        return redirect('user_login')

    return render(request, 'html/signup.html')
@login_required
def acces_profile(request,user):
    return render(request, "html/profile.html",{"user":user})
def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()
        if user and check_password(password,user.password):
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('html/login.html')
        return redirect('html/profile.html')
    return render(request, "html/login.html")