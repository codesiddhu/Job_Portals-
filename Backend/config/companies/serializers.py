from rest_framework import serializers
from .models import Company


from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['id','owner','name','description','website','email','phone','logo','location','created_at','updated_at',]
        read_only_fields = ['id','owner','created_at','updated_at',]
