from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.
class Coordinatior(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Coordinatior'
        verbose_name_plural = 'Coordinatiors'
        db_table = 'coordinatiors'

    def __str__(self):
        return self.name