from django.db import models

# Create your models here.
from companies.models import Company
from django.conf import settings


class Job(models.Model):
    JOB_TYPE_CHOICES = (('FULL_TIME', 'Full Time'),('PART_TIME', 'Part Time'),('INTERNSHIP', 'Internship'),('CONTRACT', 'Contract'),)
    EXPERIENCE_CHOICES = (('FRESHER', 'Fresher'),('0-1', '0-1 Years'),('1-3', '1-3 Years'),('3-5', '3-5 Years'),('5+', '5+ Years'),)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posted_jobs')
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=20,choices=JOB_TYPE_CHOICES)
    experience = models.CharField(max_length=20,choices=EXPERIENCE_CHOICES,default='FRESHER')
    salary_min = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    salary_max = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    application_deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title