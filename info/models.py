from tabnanny import verbose
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = 'Users'
        db_table = 'users'

class Address(models.Model):
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=200)

    def __str__(self):
        return self.district

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Adresses"
        db_table = 'address'


class Contact(models.Model):
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"
        db_table = 'contact'


class Location(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = "Locations"
        db_table = 'location_type'
    
    def __str__(self):
        return self.name