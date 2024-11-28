from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator


class User(AbstractUser):
    age = models.PositiveIntegerField(validators=[MaxValueValidator(90), MinValueValidator(10)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')

    def __str__(self):
        return self.first_name