from tabnanny import verbose
from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        db_table = 'organization_type'

    def __str__(self):
        return self.name
        
           
class Designation(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'
        db_table = 'designation_type'

class Grade(models.Model):
    grade = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'
        db_table = 'grade_type'



class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField()

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
        db_table = 'gallery'


class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField()

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'
        db_table = 'notice'