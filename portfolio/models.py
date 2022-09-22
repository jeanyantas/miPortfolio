from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/image/")
    repositorio = URLField(blank=True)
    url = URLField(blank=True)
    def __str__(self):
        return f'Proyecto N° {self.id}: {self.title}'