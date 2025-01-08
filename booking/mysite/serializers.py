from os import getenv

from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']



class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class HotelSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name']


class CityListSerializers(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['city_name']



class CityDetailSerializers(serializers.ModelSerializer):
    hotel_name = HotelSimpleSerializers(many=True, read_only=True)

    class Meta:
        model = City
        fields = ['city_name', 'hotel_name' ]



class CountryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name', ]


class CountryDetailSerializers(serializers.ModelSerializer):
    city = CityListSerializers(many=True, read_only=True)


    class Meta:
        model = Country
        fields = ['country_name', 'city' ]



class HotelPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['hotel_photos']


class RoomPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = ['room_photos']



class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'status_rooms', 'room_type', 'price']



class RoomSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['price']


class RoomDetailSerializers(serializers.ModelSerializer):
    room_images = RoomPhotoSerializers(many=True, read_only=True)
    hotel = HotelSimpleSerializers()

    class Meta:
        model = Room
        fields = ['room_number', 'hotel', 'room_video', 'price', 'all_inclusive',
                  'status_rooms', 'room_type', 'room_images', ]




class ReviewsSerializers(serializers.ModelSerializer):
    user = UserProfileSimpleSerializers()

    class Meta:
        model = Reviews
        fields = ['id', 'user', 'stars']



class HotelListSerializers(serializers.ModelSerializer):
    country = CountryListSerializers()
    city = CityListSerializers()
    hotel_images = HotelPhotoSerializers(many=True, read_only=True)
    hotel_ratings = ReviewsSerializers(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    hotel_rooms = RoomSimpleSerializers(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'hotel_stars',
                  'hotel_images', 'hotel_ratings', 'get_avg_rating', 'hotel_rooms']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

class HotelDetailSerializers(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializers()
    country = CountryListSerializers()
    city = CityListSerializers()
    hotel_rooms = RoomSerializers(many=True, read_only=True)
    created_date = serializers.DateTimeField(format=('%Y-%m-%d %H:%M'))



    class Meta:
        model = Hotel
        fields = ['hotel_name', 'owner', 'country', 'city', 'hotel_description',
                  'address', 'hotel_stars', 'hotel_video', 'hotel_rooms', 'created_date']



class BookingSerializers(serializers.ModelSerializer):
    check_in = serializers.DateTimeField(format('%Y-%m-%d %H:%M'))
    check_out = serializers.DateTimeField(format('%Y-%m-%d %H:%M'))
    hotel_booking = HotelSimpleSerializers()
    room_booking = RoomSimpleSerializers()
    user_booking = UserProfileSimpleSerializers()

    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'total_price', 'hotel_booking', 'room_booking', 'user_booking']








