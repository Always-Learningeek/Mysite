from django.shortcuts import render
from blog.models import Post
from django.utils import timezone


def index_view(request, cat_name=None):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'website/index.html', context)


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    return render(request, 'website/contact.html')

def testing_view(request):
    context={
        'fname':'hasan',
        'lname':'karimi',
    }
    return render(request,'website/test.html',context)
