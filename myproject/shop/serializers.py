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


class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['contact_info']


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['services_name', 'servicesImage', 'price']


class CatalogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['catalog_name', 'catalogImage', 'price']


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
    crated_date = serializers.DateTimeField(format='%d-%m-%Y ' '%H:%M')
    class Meta:
        model = Review
        fields = ['client', 'servise', 'master', 'comment', 'crated_date']


class CartItemSerializers(serializers.ModelSerializer):
    servise = ServicesSerializers(read_only=True)
    class Meta:
        model = CartItem
        fields = ['servise', 'quantity']



class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializers(read_only=True, many=True)
    total_price = serializers.SerializerMethodField()
    user = UserSerializers(read_only=True)
    class Meta:
        model = Cart
        fields = ['user', 'total_price', 'items']

    def get_total_price(self, obj):
        return obj.get_total_price()


# class MainPage(serializers.ModelSerializer):
#     class Meta:
#         model = Services
#         fields = ['']