from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Places(models.Model):
    title = CharField(max_length=150, verbose_name='place')

    def __str__(self):
        return self.title
