from django.db import models


class Article(models.Model):
    foto = models.ImageField(upload_to="images/")
    judul = models.CharField(max_length=300)
    isi = models.TextField()
