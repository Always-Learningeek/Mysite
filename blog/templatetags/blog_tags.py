from django import template
from blog.models import Post, Category
from django.utils import timezone


register = template.Library()


@register.inclusion_tag("blog/blog-latest-posts.html")
def latest_posts(arg=4):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag("blog/blog-categories.html")
def postcategories():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    categories = Category.objects.all()
    cat_dict={}
    for cat in categories:
        cat_dict[cat]=posts.filter(category=cat).count()
    return {'categories':cat_dict}
