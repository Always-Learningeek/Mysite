from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    form = AuthenticationForm(request, data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    return render(request, 'accounts/signup.html')
