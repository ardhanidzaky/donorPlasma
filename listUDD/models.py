from django.db import models

class Stok(models.Model):
    namaUDD = models.CharField(max_length=100)
    alamatUDD = models.CharField(max_length=100)
    nomorUDD = models.CharField(max_length=100)
    goldar = models.CharField(max_length=100)
    JumlahStok= models.IntegerField()

class StokB(models.Model):
    namaUDD = models.CharField(max_length=100)
    alamatUDD = models.CharField(max_length=100)
    nomorUDD = models.CharField(max_length=100)
    goldar = models.CharField(max_length=100)
    JumlahStok= models.IntegerField()

class StokO(models.Model):
    namaUDD = models.CharField(max_length=100)
    alamatUDD = models.CharField(max_length=100)
    nomorUDD = models.CharField(max_length=100)
    goldar = models.CharField(max_length=100)
    JumlahStok= models.IntegerField()

class StokAB(models.Model):
    namaUDD = models.CharField(max_length=100)
    alamatUDD = models.CharField(max_length=100)
    nomorUDD = models.CharField(max_length=100)
    goldar = models.CharField(max_length=100)
    JumlahStok= models.IntegerField()
