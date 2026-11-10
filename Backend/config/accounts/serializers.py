from rest_framework import serializers
from .models import User

#login 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','password','password2','role','phone',]
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return data
    def validate_role(self, value):
        if value not in ['JOB_SEEKER', 'RECRUITER']:
            raise serializers.ValidationError('Invalid user role.')
        return value
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password,**validated_data)
        return user
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {'id': self.user.id,'username': self.user.username,'email': self.user.email,'role': self.user.role,'first_name': self.user.first_name,'last_name': self.user.last_name,}
        return data