from django.urls import path
from website.views import *

urlpatterns = [
    path('blog', index),
    path('about', about),
    path('contact', contact),
]
