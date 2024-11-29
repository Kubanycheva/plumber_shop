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


class ContactInfo(models.Model):
    contact_info = PhoneNumberField()
    companyProfile = models.ForeignKey(СompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.contact_info}'


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


class Catalog(models.Model):
    catalogImage = models.ImageField(upload_to='catalog_image', null=True, blank=True)
    catalog_name = models.CharField(max_length=16, null=True, blank=True) #Каталог
    price = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.catalogImage} - {self.catalog_name}'


class Master(models.Model):
    master_name = models.CharField(max_length=16)
    image = models.ImageField(upload_to='master_image', null=True, blank=True)  #Мастер
    description = models.TextField()

    def __str__(self):
        return self.master_name


class Contact_Info(models.Model):
    contact_info = PhoneNumberField()
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Master}, {self.contact_info}'


class Gallery(models.Model):
    work_name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField()


class GlavnyiImage(models.Model):
    image = models.ImageField(upload_to='image', null=True, blank=True) #Галлерея
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='gallery')


class Review(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    servise = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service_name_service', null=True, blank=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='master_name_master', null=True, blank=True)
    comment = models.TextField()
    crated_date = models.DateTimeField(auto_now_add=True)  # Комментарии

    def __str__(self):
        return f'{self.client} - {self.master}'


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    date = models.DateTimeField(auto_now_add=True)   #Корзина

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    servise = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='cart_servise')
    quantity = models.PositiveSmallIntegerField(default=1) # Вторая корзина

    def get_total_price(self):
       return self.servise.price * self.quantity


#
# DRF.
# Filter (сatalog)
# Order (price)
# Sagger
# Permission
# Jwt
# Req.txt