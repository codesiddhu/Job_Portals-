from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer


class Company_ListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    parser_classes = [IsAuthenticated]
    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)
    def perform_create(self,serializers):
        return serializers.save(owner = self.request.user)  

class Company_DetailView(generics.RetrieveAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Company.objects.filter(owner = self.request.user)

