from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Serie(models.Model):
    name = models.CharField(max_length=200)
    airing_at = models.DateTimeField()
    rate = models.DecimalField(max_digits=12, decimal_places=2)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
