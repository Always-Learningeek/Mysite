from django.shortcuts import render


def login_view(request):
    if request.user.is_authenticated:
        msg = 'You are already logged in!'
    else:
        msg = 'You are not logged in!'

    context = {'msg': msg}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    pass


def signup_view(request):
    return render(request, 'accounts/signup.html')
