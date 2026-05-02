from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from .models import Menu, Booking
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
def index(request):
   return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated, IsAdminUser]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
