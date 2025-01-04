from django.contrib import admin
from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_date')
    list_filter = ('published_date',)
    date_hierarchy = 'published_date'
    search_fields = ('title',)
