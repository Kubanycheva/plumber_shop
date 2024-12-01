from rest_framework.exceptions import PermissionDenied
from .models import *
from .serializers import *
from rest_framework import viewsets, generics, permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class СompanyProfileViewSet(generics.ListAPIView):
    queryset = СompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializers


class СompanyProfileImageViewSet(generics.ListAPIView):
    queryset = СompanyProfileImage.objects.all()
    serializer_class = СompanyProfileImageSerializers


class ServicesViewSet(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers

class MasterViewSet(generics.ListAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializers


class GlavnyiImageViewSet(generics.ListAPIView):
    queryset = GlavnyiImage.objects.all()
    serializer_class = GlavnyiImageSerializers


class GalleryViewSet(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers



class ReviewListCreateAPIView(generics.ListCreateAPIView):
    """
    Представление для получения списка комментариев и создания нового.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.AllowAny]  # Все могут читать и создавать


class ReviewDestroyAPIView(generics.RetrieveDestroyAPIView):
    """
    Представление для удаления комментария.
    Удалять может только автор комментария.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def perform_destroy(self, instance):
        # Проверяем, что имя автора совпадает с переданным
        author_name = self.request.data.get('username', '').strip()
        if instance.author_name != author_name:
            raise PermissionDenied("You can only delete your own comments. " 
                                   "Вы можете удалять только свои собственные комментарии")
        instance.delete()