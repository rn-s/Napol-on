from django.contrib.gis.db import models


class Shop(models.Model):
    db_table = 'shop'
    name = models.CharField(max_length=255)
    geometry = models.PointField(srid=4326)

