from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Application
from .serializers import ApplicationSerializer


class ApplyJobView(generics.CreateAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        job = serializer.validated_data['job']

        if not job.is_active:
            raise PermissionDenied("This job is no longer active.")

        serializer.save(applicant=self.request.user)


class MyApplicationsView(generics.ListAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user
        ).select_related('job', 'job__company')


class RecruiterApplicationsView(generics.ListAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            job__owner=self.request.user
        ).select_related('applicant', 'job', 'job__company')


class ApplicationStatusUpdateView(generics.UpdateAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['patch', 'options', 'head']

    def get_queryset(self):
        return Application.objects.filter(
            job__owner=self.request.user
        )

    def perform_update(self, serializer):
        serializer.save()
