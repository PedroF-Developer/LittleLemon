from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class APIMessageTesting(APITestCase):
    def setUp(self):
        self.url = reverse("message_test")
    
    def test_get_message_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_message_authenticated(self):
        user = User.objects.create_user(username="test",password="test")
        self.client.force_login(user=user)
        response = self.client.get(self.url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['message'], "This view is protected")