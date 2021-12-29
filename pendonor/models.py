from django.db import models
from django.contrib.auth.models import User
from cariDonor.models import Provinsi, Kota

# Create your models here.
pilihan_goldar = (
    ("A", "A"),
    ("B", "B"),
    ("AB", "AB"),
    ("O", "O"),
)
pil_rhesus = (
    ("+","+"),
    ("-","-"),
)

class pendonor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    nama = models.CharField(max_length=63)
    NIK = models.CharField(max_length=20)
    tanggal_lahir = models.DateField()
    golongan_darah = models.CharField(max_length=2,choices=pilihan_goldar)
    rhesus = models.CharField(max_length=1,choices=pil_rhesus)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE, default="")
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE, default="")
    nomor_hp = models.CharField(max_length=20)
    bukti_swab_positif = models.CharField(max_length=100)
    bukti_swab_negatif = models.CharField(max_length=100)
    tanggal_sembuh = models.DateField()
    tanggal_terakhir_mendonor = models.DateField()

    def __str__(self):
        return self.nama
