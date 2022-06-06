from pyexpat import model
from django.db import models


class Test(models.Model):
    """Celery testing model"""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Position(models.Model):
    """Info from the API model"""
    name = models.CharField(max_length=200)
    image = models.URLField()
    price = models.CharField(max_length=200)
    rank = models.CharField(max_length=10)
    market_cap = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)