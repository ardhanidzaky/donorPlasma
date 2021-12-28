from django.db import models
from django import forms
from django.core.validators import MaxValueValidator
from cariDonor.models import Provinsi, Kota

pilihangoldar = (
    ("A", "A"),
    ("B", "B"),
    ("AB", "AB"),
    ("O", "O"),
)
class CariDonor(models.Model):
    nama = models.CharField(max_length=63)
    NIK = models.CharField(max_length=100)
    tanggal_Lahir = models.DateField()
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE, default="")
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE, default="")
    nomor_Telepon = models.CharField(max_length=15)
    golongan_Darah = models.CharField(max_length=2, choices=pilihangoldar)

    def __str__(self):
        return self.nama

    class Meta:
        unique_together = ('nama', 'NIK',)
