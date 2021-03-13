from django.db import models


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name='Место')

    def __str__(self):
        return self.title


class ImagesPlace(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, verbose_name='Место'
    )
    image = models.ImageField(
        upload_to='', null=True, blank=True, verbose_name='Изображение'
    )
    index_number = models.IntegerField(default=1, verbose_name='№ п/п')

    def __str__(self):
        return f'{self.index_number}. {self.place}'
