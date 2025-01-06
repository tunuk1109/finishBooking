from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField



class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                        MaxValueValidator(105)], null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    ROLE_CHOICES = [
        ('client', 'client'),
        ('administrator', 'administrator'),
        ('owner', 'owner')
    ]
    role = models.CharField(choices=ROLE_CHOICES, max_length=16, default='client')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='city')
    city_name = models.CharField(max_length=32)

    def __str__(self):
        return self.city_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=32)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='hotel_names')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotel_name')
    address = models.TextField()
    hotel_stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    hotel_video = models.FileField(upload_to='hotel_video/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.hotel_name} - {self.country} - {self.city}'

    def get_avg_rating(self):
        rating = self.hotel_ratings.all()
        if rating.exists():
            return round(sum([i.stars for i in rating]) / rating.count(), 1)


class HotelPhoto(models.Model):
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')
    hotel_photos = models.ImageField(upload_to='hotel_image/')


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_rooms')
    room_number = models.PositiveSmallIntegerField()
    room_video = models.FileField(upload_to='room_video/')
    price = models.PositiveSmallIntegerField()
    all_inclusive = models.TextField()
    STATUS_CHOICES = (
        ('free', 'free'),
        ('booked', 'booked'),
        ('occupied', 'occupied')
    )
    TYPE_CHOICES = (
        ('luxury', 'luxury'),
        ('single', 'single'),
        ('family', 'family'),
        ('double', 'double')
    )
    status_rooms = models.CharField(choices=STATUS_CHOICES, max_length=16, default='free')
    room_type = models.CharField(choices=TYPE_CHOICES, max_length=16, default='single')

    def __str__(self):
        return f'{self.room_number}'


class RoomPhoto(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_images')
    room_photos = models.ImageField(upload_to='room_images/')


class Booking(models.Model):
    hotel_booking = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_booking = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_booking = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    total_price = models.PositiveSmallIntegerField(default=0)
    CONFIRMATION_STATUS = [
        ('confirmed', 'confirmed'),
        ('unconfirmed', 'unconfirmed')
    ]
    status_confirmed = models.CharField(choices=CONFIRMATION_STATUS, max_length=16, default='unconfirmed')


class Reviews(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_reviews = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_ratings')
    room_reviews = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices = [(i, str(i)) for i in range(1, 11)], null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'








