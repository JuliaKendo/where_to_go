from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html
from .models import Place, ImagesPlace


class ImagesPlaceInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = ImagesPlace
    readonly_fields = ('preview_field',)
    fields = (('place', 'image'), 'preview_field', 'index_number')

    def preview_field(self, instance):
        return format_html('<img src={} height=100px />', instance.image.url)


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImagesPlaceInLine]


# Register your models here.
admin.site.register(Place, PlaceAdmin)
admin.site.register(ImagesPlace)
