from django.urls import path
from website.views import *
from blog.views import blog_single, blog_view

app_name = 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('<int:pid>', blog_single, name='blog-single'),
    path('category/<str:cat_name>', blog_view, name='website-category'),
    path('about', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('newsletter/', newsletter_view, name='newsletter'),
    path('test/', testing_view, name='test'),
]
