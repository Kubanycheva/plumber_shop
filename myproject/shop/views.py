from .models import *
from .serializers import *
from rest_framework import viewsets, generics


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class СompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = СompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializers


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializers


class СompanyProfileImageViewSet(viewsets.ModelViewSet):
    queryset = СompanyProfileImage.objects.all()
    serializer_class = СompanyProfileImageSerializers


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializers


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


class CartViewSet(generics.ListAPIView):
    serializer_class = CartSerializers

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers


    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)