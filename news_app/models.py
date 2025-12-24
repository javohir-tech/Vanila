from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import ProfileModel
# from .managers import PublishedManager

class PublishedManager(models.Manager) :
    def get_queryset(self):
        return super().get_queryset().filter(status  =  New.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class New(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to="news/images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.Draft
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("news_detail" , kwargs={'slug' : self.slug})
    


class Contact(models.Model):
    name =  models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()
    
    def __str__(self):
        return self.email
    
class Comment(models.Model) :
    user  = models.ForeignKey(User ,  on_delete=models.CASCADE , related_name='comments')
    news = models.ForeignKey(New , on_delete=models.CASCADE , related_name='comments')
    body  = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta :
        ordering = ['created_time' ,]
        
    def __str__(self):
        return f"{self.body}"