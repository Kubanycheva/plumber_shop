from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class СompanyProfile(models.Model):
    company_name = models.CharField(max_length=16)
    description = models.TextField()
    experience = models.SmallIntegerField()
    masters = models.SmallIntegerField()
    clients = models.SmallIntegerField()
    image = models.ImageField(upload_to='company_image/', null=True, blank=True)

    def __str__(self):
        return self.company_name

class Master(models.Model):
    service = models.CharField(max_length=32)
    master_name = models.CharField(max_length=16)
    image = models.ImageField(upload_to='master_image', null=True, blank=True)  #Мастер
    description = models.TextField()
    company = models.ForeignKey(СompanyProfile, on_delete=models.CASCADE, related_name='company')

    def __str__(self):
         return self.master_name


class Services(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='services')
    services_name = models.CharField(max_length=16)   #Услуги
    description = models.TextField()

    def __str__(self):
        return self.services_name


class Servise_type(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=65)
    price = models.PositiveSmallIntegerField()


class Contact_Info(models.Model):
    name = models.CharField(max_length=32)
    contact_info = PhoneNumberField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


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