from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'booking', BookingViewSet, basename='booking_list'),
router.register(r'reviews', ReviewsViewSet, basename='reviews_list')


urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='users_detail'),
    path('country/', CountryListAPIViewSet.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIViewSet.as_view(), name='country_detail'),
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
    path('room/', RoomAPIView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomDetailAPIView.as_view(), name='room_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]