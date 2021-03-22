from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name='Место')
    title_short = models.CharField(
        max_length=50, blank=True, verbose_name='Сокращенное наименование'
    )
    description_long = HTMLField(blank=True, verbose_name='Описание')
    description_short = models.TextField(
        blank=True, verbose_name='Сокращенное описание'
    )
    lng = models.FloatField(verbose_name='Долгота', default=0.0, blank=True)
    lat = models.FloatField(verbose_name='Широта', default=0.0, blank=True)

    class Meta(object):
        ordering = ['id']

    def __str__(self):
        return self.title


class ImagesPlace(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, verbose_name='Место'
    )
    image = models.ImageField(
        upload_to='', verbose_name='Изображение'
    )
    index_number = models.PositiveIntegerField(
        default=0, blank=True, verbose_name='№ п/п'
    )

    class Meta(object):
        ordering = ['index_number']

    def __str__(self):
        return f'{self.index_number}. {self.place}'
