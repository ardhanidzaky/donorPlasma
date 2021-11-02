from django.db import models


class faq(models.Model):
    question = models.CharField(max_length=1000,  default='SOME STRING')
    answer = models.TextField(max_length=1000,  default='SOME STRING')