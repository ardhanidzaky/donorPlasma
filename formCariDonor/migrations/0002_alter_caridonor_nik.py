# Generated by Django 3.2.7 on 2021-12-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formCariDonor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caridonor',
            name='NIK',
            field=models.CharField(max_length=100),
        ),
    ]
