# Generated by Django 4.1.2 on 2022-10-29 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='batch',
        ),
    ]
