from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (('JOB_SEEKER', 'Job Seeker'),('RECRUITER', 'Recruiter'),('ADMIN', 'Admin'),)

    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='JOB_SEEKER')
    phone = models.CharField(max_length=15,blank=True,null=True)
    profile_image = models.ImageField(upload_to='profile_images/',blank=True,null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username