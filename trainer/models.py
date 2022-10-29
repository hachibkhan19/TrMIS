from tabnanny import verbose
from django.db import models
from info.models import Address, Contact
from batch.models import Batch

# Create your models here.
class Trainer(models.Model):
    nid = models.CharField(max_length=200)
    batch = models.ManyToManyField(Batch)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'
        db_table = 'trainer'