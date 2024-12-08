from rest_framework.exceptions import PermissionDenied
from .models import *
from .serializers import *
from rest_framework import viewsets, generics, permissions


class СompanyProfileViewSet(generics.ListAPIView):
    queryset = СompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializers


class СompanySimpleProfileViewSet(generics.ListAPIView):
    queryset = СompanyProfile.objects.all()
    serializer_class = CompanySimpleProfileSerializers


class ServicesViewSet(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers


class ServicesMoreViewSet(generics.ListAPIView):
    queryset = Servise_type.objects.all()
    serializer_class = ServiceMoreSerializers


class MasterViewSet(generics.ListAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializers


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewGetSerializers

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