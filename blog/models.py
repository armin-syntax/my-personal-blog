from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.get_short_name()

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_short_name(self):
        return f"{self.name[:50]}..." if len(self.name) > 50 else self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.get_short_title()

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_short_title(self):
        return f"{self.title[:50]}..." if len(self.title) > 50 else self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])
