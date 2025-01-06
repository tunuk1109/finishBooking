from rest_framework import viewsets, generics, permissions, status
from .serializers import *
from .models import *
from .permissions import CheckUserRating
from .paginations import RoomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)




class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)



class CountryListAPIViewSet(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CountryDetailAPIViewSet(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['country', 'city']
    search_fields = ['hotel_name']
    ordering_fields = ['city_name']



class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = RoomPagination



class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [CheckUserRating, permissions.IsAuthenticatedOrReadOnly]