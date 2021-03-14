from django.contrib import admin
from .models import Place, ImagesPlace


class ImagesPlaceInLine(admin.TabularInline):
    model = ImagesPlace


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImagesPlaceInLine]


# Register your models here.
admin.site.register(Place, PlaceAdmin)
admin.site.register(ImagesPlace)
