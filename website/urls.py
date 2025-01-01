from django.urls import path
from website.views import *

urlpatterns = [
    path('', index),
    path('about', about),
    path('contact', contact),
]
