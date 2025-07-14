from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class InstaUser(AbstractUser):
    username=models.CharField(max_length=100, default='', unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=500,blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    dob = models.DateField(default=datetime.date(2025, 1, 1))
    website = models.URLField(blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True)
    is_private = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    account_type = models.CharField(max_length=20, default='personal')
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    posts_count = models.PositiveIntegerField(default=0)
    two_factor_enabled = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    gmail = models.EmailField(default='')
