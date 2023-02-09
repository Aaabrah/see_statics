from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from .models import UserModel
from django.contrib.auth import login, logout, authenticate


def registration_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        print(form)
        if form.is_valid():
            user = UserModel(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('main:home')

    return render(request, 'auth-register.html', context={
        'registration_form': form
    })


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if not user is None:
                login(request, user)
                return redirect('main:home')
    return render(request, 'auth-login.html', context={
        'login_form': form
    })


def logout_view(request):
    logout(request)
    return redirect('users:login')
