# Generated by Django 3.2.7 on 2021-11-02 16:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cariDonor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CariDonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=63)),
                ('NIK', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999999)])),
                ('tanggal_Lahir', models.DateField()),
                ('nomor_Telepon', models.CharField(max_length=15)),
                ('golongan_Darah', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2)),
                ('kota', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cariDonor.kota')),
                ('provinsi', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cariDonor.provinsi')),
            ],
            options={
                'unique_together': {('nama', 'NIK')},
            },
        ),
    ]
