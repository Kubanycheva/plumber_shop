from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator


class User(AbstractUser):
    age = models.PositiveIntegerField(validators=[MaxValueValidator(90), MinValueValidator(10)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')  # Админ

    def __str__(self):
        return self.first_name


class СompanyProfile(models.Model):
    company_name = models.CharField(max_length=16)
    company_image = models.ImageField(upload_to='company_image')  # О компании
    description = models.TextField()

    def str(self):
        return self.company_name


class ContactInfo(models.Model):
    contact_info = PhoneNumberField()
    companyProfile = models.ForeignKey(СompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.СompanyProfile}, {self.contact_info}'


class СompanyProfileImage(models.Model):
    company_image = models.ForeignKey(СompanyProfile, on_delete=models.CASCADE, related_name='company_images')
    image = models.ImageField(upload_to='company_image')  #Изображения компании


class Services(models.Model):
    servicesImage = models.ImageField(upload_to='services_image')
    services_name = models.CharField(max_length=16)   #Услуги
    price = models.PositiveSmallIntegerField()
    description = models.TextField

    def __str__(self):
        return f'{self.servicesImage} - {self.services_name}'


class ServicesProfileImage(models.Model):
    company_image = models.ForeignKey(СompanyProfile, on_delete=models.CASCADE, related_name='services_images')
    image = models.ImageField(upload_to='services_image')  #изображения услугии


class Catalog(models.Model):
    catalogImage = models.ImageField(upload_to='catalog_image')
    catalog_name = models.CharField(max_length=16, null=True, blank=True) #Каталог
    price = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.catalogImage} - {self.catalog_name}'


class СatalogProfileImage(models.Model):
    company_image = models.ForeignKey(СompanyProfile, on_delete=models.CASCADE, related_name='company_images')
    image = models.ImageField(upload_to='company_image', null=True, blank=True)  #Каталог изображения


class Master(models.Model):
    master_name = models.CharField(max_length=16)
    image = models.ImageField(upload_to='master_image')  #Мастер
    description = models.TextField()

    def __str__(self):
        return self.master_name


class ContactInfo(models.Model):
    contact_info = PhoneNumberField()
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Master}, {self.contact_info}'


class Image(models.Model):
    image = models.ImageField(upload_to='image')  #Изображения


class Gallery(models.Model):
    company_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='image', null=True, blank=True) #Галлерея


class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    servise = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service_name', null=True, blank=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='master_name', null=True, blank=True)
    comment = models.TextField()
    crated_date = models.DateTimeField(auto_now_add=True)  # Галлерея

    def __str__(self):
        return f'{self.comment} - {self.crated_date}'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    date = models.DateTimeField(auto_now_add=True)   #Корзина

    def __str__(self):
        return f'{self.user}'


class CartItem(models.Model):
    cart = models.
    servise
    quantity
    total_price

#
# DRF.
# Env
# Language
# Filter (сatalog)
# Order (price)
# Sagger
# Permission
# Jwt
# Req.txt