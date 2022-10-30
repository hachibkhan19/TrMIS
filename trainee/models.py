from email.policy import default
from tabnanny import verbose
from django.db import models
from info.models import Address, Contact

# Create your models here.
class Trainee(models.Model):
    name = models.CharField(max_length=200, default="Hasib")
    nid = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.nid

    class Meta:
        verbose_name = 'Trainee'
        verbose_name_plural = 'Trainees'
        db_table = 'trainee'
        