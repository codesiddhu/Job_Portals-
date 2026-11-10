from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Job
from .serializers import JobSerializer



class JobListCreateView(generics.ListCreateAPIView):

    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_queryset(self):
        queryset = Job.objects.filter(
            is_active=True
        ).select_related('company', 'owner')

        search = self.request.query_params.get('search')
        location = self.request.query_params.get('location')
        job_type = self.request.query_params.get('job_type')
        experience = self.request.query_params.get('experience')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if location:
            queryset = queryset.filter(location__icontains=location)

        if job_type:
            queryset = queryset.filter(job_type=job_type)

        if experience:
            queryset = queryset.filter(experience=experience)

        return queryset

    def perform_create(self, serializer):
        company = serializer.validated_data['company']

        if company.owner != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied(
                "You can only post jobs for your own company."
            )

        serializer.save(owner=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        queryset = Job.objects.select_related('company', 'owner')

        if self.request.method == 'GET':
            return queryset.filter(is_active=True)

        return queryset.filter(owner=self.request.user)
