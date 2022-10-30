from email.policy import default
from tabnanny import verbose
from django.db import models
from info.models import Address, Contact

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=200, default='ajom khan')
    nid = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'
        db_table = 'trainer'
