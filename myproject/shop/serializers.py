from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class СompanyProfileImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = СompanyProfileImage
        fields = ['image']


class CompanyProfileSerializers(serializers.ModelSerializer):
    company_profile_images = СompanyProfileImageSerializers(read_only=True, many=True)
    class Meta:
        model = СompanyProfile
        fields = ['company_name', 'company_profile_images', 'description']


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['services_name', 'servicesImage', 'price']


class MasterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ['master_name', 'image', 'description']


class GlavnyiImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = GlavnyiImage
        fields = ['image']


class GallerySerializers(serializers.ModelSerializer):
    gallery = GlavnyiImageSerializers(read_only=True, many=True)
    class Meta:
        model = Gallery
        fields = ['work_name', 'description']


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author_name', 'servise', 'master', 'comment']



# class MainPage(serializers.ModelSerializer):
#     class Meta:
#         model = Services
#         fields = ['']