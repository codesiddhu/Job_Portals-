
from django.urls import path
from .views import Company_DetailView,Company_ListView

urlpatterns =[
    path("listapi/",Company_ListView.as_view(),name="company-list"),
    path("listapi/<int:pk>/",Company_DetailView.as_view(),name="company-detail")
]