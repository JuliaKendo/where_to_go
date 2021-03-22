from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html
from .models import Place, ImagesPlace


class ImagesPlaceInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = ImagesPlace
    extra = 0
    readonly_fields = ('preview_field',)
    fields = (('place', 'image'), 'preview_field', 'index_number')

    def preview_field(self, instance):
        if instance.image:
            return format_html('<img src={} height=100px />', instance.image.url)
        return 'Здесь будет превью, когда вы выберете файл'


class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImagesPlaceInLine]
    search_fields = ['title']


# Register your models here.
admin.site.register(Place, PlaceAdmin)
admin.site.register(ImagesPlace)
