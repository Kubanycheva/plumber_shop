from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    age = models.SmallIntegerField(validators=[MaxValueValidator(80),
                                               MinValueValidator(18)], null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')  # Админ

    def __str__(self):
        return self.first_name


class СompanyProfile(models.Model):
    company_name = models.CharField(max_length=16)
    description = models.TextField()

    def __str__(self):
        return self.company_name


class СompanyProfileImage(models.Model):
    company_image = models.ForeignKey(СompanyProfile, on_delete=models.CASCADE, related_name='company_profile_images')
    image = models.ImageField(upload_to='company_image', null=True, blank=True)  #Изображения компании


class Services(models.Model):
    servicesImage = models.ImageField(upload_to='services_image', null=True, blank=True)
    services_name = models.CharField(max_length=16)   #Услуги
    price = models.PositiveSmallIntegerField()
    description = models.TextField()


    def __str__(self):
        return f'{self.servicesImage} - {self.services_name}'


class Master(models.Model):
    master_name = models.CharField(max_length=16)
    image = models.ImageField(upload_to='master_image', null=True, blank=True)  #Мастер
    description = models.TextField()

    def __str__(self):
        return self.master_name


class Contact_Info(models.Model):
    contact_info = PhoneNumberField()
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    companyProfile = models.ForeignKey(СompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Master}, {self.contact_info}'


class Gallery(models.Model):
    work_name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField()


class GlavnyiImage(models.Model):
    image = models.ImageField(upload_to='image', null=True, blank=True) #Галлерея
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='gallery')


class Review(models.Model):
    author_name = models.CharField(unique=True, max_length=52)
    servise = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service_name_service', null=True, blank=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='master_name_master', null=True, blank=True)
    comment = models.TextField()
    crated_date = models.DateTimeField(auto_now_add=True)  # Комментарии

    def __str__(self):
        return f'{self.author_name} - {self.master}'




#
# DRF.
# Filter (сatalog)
# Order (price)
# Sagger
# Permission
# Jwt
# Req.txt