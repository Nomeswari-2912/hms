from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name
