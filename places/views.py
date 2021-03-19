from django.http import JsonResponse
from django.shortcuts import (
    render, get_object_or_404, get_list_or_404
)
from .models import Place, ImagesPlace


def get_features(place):
    images = get_list_or_404(
        ImagesPlace.objects.order_by('index_number'), place=place
    )
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
        },
        "properties": {
            "title": place.title_short,
            "placeId": place.id,
            "details": {
                "title": place.title,
                "imgs": [item.image.url for item in images],
                "description_short": place.description_short,
                "description_long": place.description_long,
                "coordinates": {
                    "lng": place.lng,
                    "lat": place.lat
                }
            }
        }
    }


def index(request):
    places = Place.objects.all()
    return render(
        request, 'index.html', {
            'places': {
                "type": "FeatureCollection",
                "features": [get_features(place) for place in places]
            }
        }
    )


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return JsonResponse(
        get_features(place),
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )
