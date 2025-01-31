from django import template
from blog.models import Post, Category
from django.utils import timezone


register = template.Library()


@register.inclusion_tag('website/blog_latest_posts_in_website.html')
def blog_latest_posts_in_website(arg=6):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    latest_posts= posts.order_by('-published_date')[:arg]
    categories = Category.objects.all()
    cat_dict={}
    for cat in categories:
        cat_dict[cat]=posts.filter(category=cat).count()
    context = {'latest_posts':latest_posts, 'categories':cat_dict}
    return (context)
