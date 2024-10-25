from django.db import models

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.name

