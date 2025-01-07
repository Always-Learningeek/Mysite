from django.db import models
from django.contrib.auth.models import User

class Post (models.Model):
    author=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to = 'blog/', default='blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    #category = models.CharField(max_length=255)
    #tags = models.CharField(max_length=255)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f"{self.title}-{self.id}"
