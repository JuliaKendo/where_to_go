import os
import requests
from django.db.models import Max
from django.core.files.base import ContentFile
from django.core.management import BaseCommand, CommandError
from places.models import Place, ImagesPlace


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('loadable_file', type=str)

    def handle(self, *args, **options):
        try:
            load_place(options['loadable_file'])
        except Exception as error:
            raise CommandError(f'Ошибка загрузки файла: {error}')


def load_place(loadable_file):
    response = requests.get(loadable_file)
    response.raise_for_status()
    place_info = response.json()
    place_entry = handle_place(
        **{key: value for key, value in place_info.items() if key != 'imgs'}
    )
    handle_images(place_entry, place_info['imgs'])


def handle_place(title, description_short, description_long, coordinates):
    place, _ = Place.objects.get_or_create(
        title=title,
        title_short=title,
        description_long=description_long,
        description_short=description_short,
        lng=float(coordinates['lng']), lat=float(coordinates['lat'])
    )
    return place


def handle_images(place, images):
    for image_path in images:
        file_name = os.path.basename(image_path)
        response = requests.get(image_path)
        response.raise_for_status()
        image_entry, create = ImagesPlace.objects.filter(
            image__icontains=file_name
        ).get_or_create(place=place)
        if create:
            image_entry.index_number = get_index_number(place)
        image_entry.image.save(file_name, ContentFile(response.content))
        image_entry.save()


def get_index_number(place):
    max_num_entry = ImagesPlace.objects.filter(
        place=place
    ).aggregate(Max('index_number'))['index_number__max']
    return max_num_entry + 1
