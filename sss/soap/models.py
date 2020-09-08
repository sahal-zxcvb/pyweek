from django.db import models

class certificate(models.Model):
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    college=models.CharField(max_length=200)
    hash=models.CharField(max_length=300)

    def __str__(self):
        return self.name
