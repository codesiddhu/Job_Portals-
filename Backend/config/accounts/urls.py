from .views import (RegisterView,LoginView,ProfileSerializerView,LogoutView)
from rest_framework_simplejwt.views import TokenRefreshView

from django.urls import path,include

urlpatterns = [
    
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('profile/',ProfileSerializerView.as_view(),name='profile'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]