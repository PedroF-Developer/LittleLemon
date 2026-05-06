from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream",price=80,inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTest(TestCase):
    def test_get_booking(self):
        booking = Booking.objects.create(name="Robert",no_of_guests=4,booking_date="2026-05-04")
        self.assertEqual(str(booking), "Booking for Robert")