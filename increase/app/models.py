from django.db import models


# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=100)
    ph = models.CharField(max_length=100)
    about = models.CharField(max_length=100, default='null')
    email = models.EmailField(primary_key=True, max_length=100, default='null')

    def __str__(self):
        return self.email


class login(models.Model):
    email = models.EmailField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

    def __str__(self):
        return self.email
