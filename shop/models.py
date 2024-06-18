from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"(pk={self.pk}, title={self.title!r})"


class Game(models.Model):
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name="games", blank=True)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    size = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    on_sale = models.BooleanField(default=False)

    def __str__(self):
        return f"(pk={self.pk}, title={self.title!r})"


