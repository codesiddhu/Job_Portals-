from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer,CustomTokenObtainPairSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
class ProfileSerializerView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({'id': user.id,'username': user.username,'email': user.email,'role': user.role,'first_name': user.first_name,'last_name': user.last_name,'phone': user.phone,'bio': user.bio,'location': user.location,})
      
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error': 'Refresh token is required.'},status=400)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successfully logged out.'})
        except Exception:
            return Response({'error': 'Invalid refresh token.'},status=400)