from django.shortcuts import render
from .models import Place


def get_places():
    features = []
    places = Place.objects.all()
    for place in places:
        features.append({
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
                    "imgs": [
                        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
                        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
                        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
                        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
                        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
                        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
                    ],
                    "description_short": place.description_short,
                    "description_long": place.description_long,
                    "coordinates": {
                        "lng": place.lng,
                        "lat": place.lat
                    }
                }
            }
        })

    return {
        "type": "FeatureCollection",
        "features": features
    }


def index(request):
    return render(
        request, 'index.html',
        {'places': get_places()}
    )
