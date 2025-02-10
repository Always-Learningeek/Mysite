from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from accounts.forms import  CustomUserCreationForm, CustomAuthenticationForm

'''
@csrf_protect
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = None
                if '@' in username_or_email:
                    try:
                        user_with_email = User.objects.get(email=username_or_email)
                        user = authenticate(request, username=user_with_email.username, password=password)
                        messages.success(request, 'Login via email successful!.')
                    except User.DoesNotExist:
                        user = None
                if user is None:
                    user = authenticate(request, username=username_or_email, password=password)
                    if user:
                        messages.success(request, 'Logged in successfully.')
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid credentials or form.')
            else:
                context = {'form': form, 'error': 'Invalid credentials or form'}
                return render(request, 'accounts/login.html', context)
        else:
            form = AuthenticationForm()
            context = {'form': form}
            return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')
'''

@csrf_protect
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get('username_or_email')
                password = form.cleaned_data.get('password')
                try:
                    if '@' in username_or_email:
                        user = User.objects.get(email=username_or_email)
                    else:
                        user = User.objects.get(username=username_or_email)
                    user = authenticate(request, username=user.username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Login successful!')
                        return redirect('/')
                    else:
                        messages.error(request, 'Invalid credentials.')
                except User.DoesNotExist:
                    messages.error(request, 'User with this email or username does not exist.')
            else:
                messages.error(request, 'Invalid form.')
        else:
            form = CustomAuthenticationForm()

        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')



@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

'''
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if email and '@' in email:
                user = form.save(commit=False)
                user.email = email
                user.save()
                login(request, user)
                return redirect('/')
            else:
                user = form.save()
                login(request, user)
                return redirect('/')
        else:
            return redirect('/')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
'''

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    else:
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)