from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('home', blog_view, name='blog-home'),
    path('single', blog_single, name='blog-single'),
    path('test', test, name='test'),

]
