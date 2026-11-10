from django.contrib import admin

# Register your models here.
from .models import Company


class Company_admin(admin.ModelAdmin):
    list_display = ["owner","name","description","website","email","phone","logo","location","created_at","updated_at"]
admin.site.register(Company,Company_admin)
