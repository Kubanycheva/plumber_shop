from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='users')
router.register(r'company', СompanyProfileViewSet, basename='company_profile')
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'catalog', CatalogViewSet, basename='catalog')
router.register(r'master', MasterViewSet, basename='master')
router.register(r'review', ReviewViewSet, basename='reviews')
router.register(r'contacts', ContactInfoViewSet, basename='contacts')


urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartViewSet.as_view(), name='cart')
]
