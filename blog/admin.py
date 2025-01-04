from django.contrib import admin
from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'counted_views', 'status', 'published_date', 'created_date')
    list_filter = ('status',)
    date_hierarchy = 'published_date'
    search_fields = ['title','content']
    empty_value_display = '-empty-'

