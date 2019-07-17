#Veritabanı veri modelleri

from django.db import models

class Stock(models.Model):

    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.ticker



