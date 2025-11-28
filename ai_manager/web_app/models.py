from django.db import models


class Sender(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)


class Letter(models.Model):
    author = models.ForeignKey(Sender, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)
