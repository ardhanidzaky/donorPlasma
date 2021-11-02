from django.db import models

class Provinsi(models.Model):
    nama = models.CharField(max_length=63, primary_key=True)
    def __str__(self):
        return self.nama

class Kota(models.Model):
    # id isinya f"{nama_provinsi} {2_digit_kota_keberapa}"
    id = models.CharField(primary_key=True, max_length=127)
    nama = models.CharField(max_length=63)
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama

pilihan_goldar = (
    ("A", "A"),
    ("B", "B"),
    ("AB", "AB"),
    ("O", "O"),
)
class Donor(models.Model):
    provinsi = models.ForeignKey(Provinsi, on_delete=models.CASCADE)
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE)
    goldar =  models.CharField(max_length=2, choices=pilihan_goldar)

# Ternyata ga butuh, kalo ada yg butuh, mau ganti2 silakan
class UDD(models.Model):
    nama = models.CharField(primary_key=True, max_length=63)
    stock_A = models.PositiveIntegerField(default=0)
    stock_B = models.PositiveIntegerField(default=0)
    stock_O = models.PositiveIntegerField(default=0)
    stock_AB = models.PositiveIntegerField(default=0)
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE)
