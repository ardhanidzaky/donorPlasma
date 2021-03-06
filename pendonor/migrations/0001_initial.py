# Generated by Django 3.2.7 on 2021-11-02 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cariDonor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pendonor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=63)),
                ('NIK', models.CharField(max_length=15)),
                ('tanggal_lahir', models.DateField()),
                ('golongan_darah', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2)),
                ('rhesus', models.CharField(choices=[('+', '+'), ('-', '-')], max_length=1)),
                ('nomor_hp', models.CharField(max_length=12)),
                ('bukti_swab_positif', models.FileField(null=True, upload_to='documents/')),
                ('bukti_swab_negatif', models.FileField(null=True, upload_to='documents/')),
                ('tanggal_sembuh', models.DateField()),
                ('tanggal_terakhir_mendonor', models.DateField()),
                ('kota', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cariDonor.kota')),
                ('provinsi', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cariDonor.provinsi')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
