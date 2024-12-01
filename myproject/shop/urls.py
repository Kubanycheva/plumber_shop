from django.urls import path, include
from .views import *

urlpatterns = [
    path('company/', СompanyProfileViewSet.as_view(), name='company-profile'),
    path('service/', ServicesViewSet.as_view(), name='service'),
    path('master/', MasterViewSet.as_view(), name='master'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDestroyAPIView.as_view(), name='review-destroy'),
]
