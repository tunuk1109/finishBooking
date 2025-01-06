from .models import Country, City, Hotel
from modeltranslation.translator import TranslationOptions,register


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name', )


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name', )


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_description', 'address')








