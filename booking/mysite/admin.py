from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *
from modeltranslation.admin import TranslationAdmin



@admin.register(Country, City)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto
    extra = 1


class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1


@admin.register(Hotel)
class HotelPhotoAdmin(TranslationAdmin):
    inlines = [HotelPhotoInline]


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



class RoomAdmin(ModelAdmin):
    inlines = [RoomPhotoInline]




admin.site.register(UserProfile)
admin.site.register(Booking)
admin.site.register(Room, RoomAdmin)
admin.site.register(Reviews)

