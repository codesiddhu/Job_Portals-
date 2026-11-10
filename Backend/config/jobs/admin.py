from django.contrib import admin

# Register your models here.
from .models import Job

class Job_admin(admin.ModelAdmin):
    list_display = ["owner","company","title","description","requirements","location","job_type","experience","salary_min","salary_max","is_active","application_deadline","created_at","updated_at"]
admin.site.register(Job,Job_admin)
