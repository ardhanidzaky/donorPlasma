# Generated by Django 3.2.7 on 2021-12-29 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendonor', '0002_auto_20211221_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendonor',
            name='NIK',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pendonor',
            name='nomor_hp',
            field=models.CharField(max_length=20),
        ),
    ]