from django.db import models
from django.contrib.auth.models import User, Group  
from django.utils import timezone

# Create your models here.

class EventCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EventRegion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('canceled', 'Canceled'),
        ('featured', 'featured'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateTimeField()
    registration_required = models.BooleanField(default=False)
    registration_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True)
    Region = models.ForeignKey(EventRegion, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username
