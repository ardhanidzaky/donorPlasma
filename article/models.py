from django.db import models


class Article(models.Model):
    foto = models.TextField()
    judul = models.CharField(max_length=300)
    isi = models.TextField()
