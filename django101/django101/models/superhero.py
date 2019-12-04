from django.db import models

from django101.models.power import Power


class Superhero(models.Model):
    name = models.CharField(max_length=30)
    secret_identity = models.CharField(max_length=30)
    powers = models.ManyToManyField(Power)

    class Meta:
        db_table = 'superheroes'
