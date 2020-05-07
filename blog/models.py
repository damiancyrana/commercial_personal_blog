from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PostManager(models.Manager):
    """Custom QuerySet Manager"""
    def queryset(self):
        return super(PostManager, self).queryset().filter(status='published')


class Post(models.Model):
    """Basic database model for blog posts"""
    CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    skeleton = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=CHOICES, default='draft')
    objects = models.Manager()
    published = PostManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
