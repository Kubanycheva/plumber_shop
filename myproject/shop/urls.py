from django.urls import path, include
from .views import *

urlpatterns = [
    path('company/', СompanyProfileViewSet.as_view(), name='company-profile'),
    path('company_more/', СompanySimpleProfileViewSet.as_view(), name='company_more'),
    path('service/', ServicesViewSet.as_view(), name='service'),
    path('service_more/', ServicesMoreViewSet.as_view(), name='service_more'),
    path('master/', MasterViewSet.as_view(), name='master'),
    path('reviews_list/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDestroyAPIView.as_view(), name='review-destroy'),
]
