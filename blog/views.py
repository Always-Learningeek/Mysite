from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    post.counted_views += 1
    post.save()
    previous_post = Post.objects.filter(id__lt=post.pk).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post.pk).order_by('id').first()
    context = {'post': post, 'previous_post': previous_post, 'next_post': next_post}
    return render(request, 'blog/blog-single.html', context)


def test(request):
    posts =Post.objects.filter(published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/test-blog.html', context)
