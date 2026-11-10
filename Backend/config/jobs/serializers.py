
from rest_framework import serializers
from .models import Job
from companies.models import Company


class JobSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source='company.name',read_only=True)
    class Meta:
        model = Job
        fields = ['id','owner','company','company_name','title','description','requirements','location','job_type','experience','salary_min','salary_max','is_active','application_deadline','created_at','updated_at',]
        read_only_fields = ['id','owner','created_at','updated_at',]
    def validate(self, data):
        salary_min = data.get('salary_min')
        salary_max = data.get('salary_max')
        if salary_min is not None and salary_max is not None:
            if salary_min > salary_max:
                raise serializers.ValidationError("Minimum salary cannot exceed maximum salary.")
        return data
