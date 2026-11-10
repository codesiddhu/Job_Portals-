
from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    applicant_name = serializers.CharField(source='applicant.username',read_only=True)
    job_title = serializers.CharField(source='job.title',read_only=True)
    company_name = serializers.CharField(source='job.company.name',read_only=True)

    class Meta:
        model = Application
        fields = ['id','job','job_title','company_name','applicant','applicant_name','resume','cover_letter','status','applied_at','updated_at',]
        read_only_fields = ['id','applicant','status','applied_at','updated_at',]
