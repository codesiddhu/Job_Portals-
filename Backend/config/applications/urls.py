
from django.urls import path

from .views import (
    ApplyJobView,
    MyApplicationsView,
    RecruiterApplicationsView,
    ApplicationStatusUpdateView,
)

urlpatterns = [
    path('apply/', ApplyJobView.as_view(), name='apply-job'),
    path('my-applications/', MyApplicationsView.as_view(), name='my-applications'),
    path('recruiter-applications/', RecruiterApplicationsView.as_view(), name='recruiter-applications'),
    path('<int:pk>/status/', ApplicationStatusUpdateView.as_view(), name='application-status'),
   
]
