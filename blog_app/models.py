from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_author')
    blog_title = models.CharField(max_length=250, verbose_name='Type Blog Title')
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name='Do you want to share something?')
    blog_image = models.ImageField(upload_to='blog_image', verbose_name='Blog Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.blog_title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comment')
    comment = models.TimeField()
    comment_date = models.DateTimeField(auto_now_add=True)
    
class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_user')