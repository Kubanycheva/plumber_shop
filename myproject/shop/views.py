from .models import *
from .serializers import *
from rest_framework import viewsets, generics


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class СompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = СompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializers


class СompanyProfileImageViewSet(viewsets.ModelViewSet):
    queryset = СompanyProfileImage.objects.all()
    serializer_class = СompanyProfileImageSerializers


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializers


class GlavnyiImageViewSet(viewsets.ModelViewSet):
    queryset = GlavnyiImage.objects.all()
    serializer_class = GlavnyiImageSerializers


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

