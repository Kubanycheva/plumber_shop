from rest_framework import serializers
from .models import *


class CompanyProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = СompanyProfile
        fields = ['company_name', 'description']


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['services_name', 'description']


class ServicesSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['services_name']


class ServiceMoreSerializers(serializers.ModelSerializer):
    service = ServicesSimpleSerializers(read_only=True)
    class Meta:
        model = Servise_type
        fields = ['service', 'service_type', 'price']


class MasterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ['master_name', 'image', 'service']


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author_name', 'servise', 'master', 'comment']


class ReviewGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['author_name', 'comment']


class CompanySimpleProfileSerializers(serializers.ModelSerializer):
    company = MasterSerializers(read_only=True, many=True)

    class Meta:
        model = СompanyProfile
        fields = ['company_name', 'description', 'company']

