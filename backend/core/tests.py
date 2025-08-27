from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TravelOption, Booking, UserProfile

class BookingTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.travel_option = TravelOption.objects.create(
            type='Bus', source='A', destination='B', date_time='2025-09-01 10:00', price=100, available_seats=10
        )

    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser', 'password1': 'newpass123', 'password2': 'newpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_booking(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('book_travel', args=[self.travel_option.travel_id]), {'seats': 2})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(user=self.user, travel_option=self.travel_option).exists())

    def test_cancel_booking(self):
        booking = Booking.objects.create(user=self.user, travel_option=self.travel_option, number_of_seats=1, total_price=100, status='Confirmed')
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('cancel_booking', args=[booking.booking_id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Booking.objects.filter(pk=booking.pk).exists())

    def test_profile_update(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('profile'), {
            'full_name': 'Test User', 'email': 'test@example.com', 'phone': '1234567890'
        })
        self.assertEqual(response.status_code, 302)
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.full_name, 'Test User')
        self.assertEqual(profile.email, 'test@example.com')
        self.assertEqual(profile.phone, '1234567890')
