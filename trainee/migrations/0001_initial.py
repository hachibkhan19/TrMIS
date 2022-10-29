# Generated by Django 4.1.2 on 2022-10-25 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.CharField(max_length=200)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.address')),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='info.contact')),
            ],
            options={
                'verbose_name': 'Trainee',
                'verbose_name_plural': 'Trainees',
                'db_table': 'trainee',
            },
        ),
    ]