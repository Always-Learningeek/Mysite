from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get('username', 'email')
                password = form.cleaned_data.get('password')
                if '@' in username_or_email:
                    try:
                        user = authenticate(request, username=username_or_email, password=password)
                        messages.success(request, 'Login via email successful!.')
                    except User.DoesNotExist:
                        user = None
                else:
                    user = authenticate(request, username=username_or_email, password=password)
                    messages.success(request, 'Logged in successfully.')

                if user is not None:
                    login(request, user)
                    return redirect('/')

            else:
                context = {'form': form, 'error': 'Invalid credentials or form'}
                return render(request, 'accounts/login.html', context)
        else:
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if '@' in form:
                user = form.save()
                login(request, user)
                return redirect('/')
            else:
                user = form.save()
                login(request, user)
                return redirect('/')

        else:
            #context = {'form': form}
            #return render(request, 'accounts/signup.html', context)
            return redirect('/')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


@csrf_protect
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get('username', 'email')
                password = form.cleaned_data.get('password')
                if '@' in username_or_email:
                    try:
                        user = authenticate(request, username=username_or_email, password=password)
                        messages.success(request, 'Login via email successful!.')
                    except User.DoesNotExist:
                        user = None
                else:
                    user = authenticate(request, username=username_or_email, password=password)
                    messages.success(request, 'Logged in successfully.')

                if user is not None:
                    login(request, user)
                    return redirect('/')

            else:
                context = {'form': form, 'error': 'Invalid credentials or form'}
                return render(request, 'accounts/login.html', context)
        else:
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            #context = {'form': form}
            #return render(request, 'accounts/signup.html', context)
            return redirect('/')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)


#def forgot_password_view(request):
    #x = auth_views.PasswordResetView.as_view()
    #return redirect('accounts/signup.html')
    #return render(request, 'accounts/password_reset_form.html',x)