from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from jobs.models import Job


class Application(models.Model):

    STATUS_CHOICES = (('PENDING', 'Pending'),('REVIEWED', 'Reviewed'),('SHORTLISTED', 'Shortlisted'),('REJECTED', 'Rejected'),('SELECTED', 'Selected'),)

    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='applications')
    resume = models.FileField( upload_to='resumes/')
    cover_letter = models.TextField(blank=True,default ="optional")
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('job', 'applicant')
        ordering = ['-applied_at']

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
