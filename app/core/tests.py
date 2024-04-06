from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import User, Notification
from .serializers import NotificationSerializer


# Create your tests here.
class NotificationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test data for the Notification model
        user = User.objects.create(name='Test User', email='test@example.com')
        notification_type = NotificationType.objects.create(name='Test Type')
        Notification.objects.create(category='Test Category', message='Test Message', user=user, notification_type=notification_type)

    def test_notification_str(self):
        notification = Notification.objects.get(id=1)
        self.assertEqual(str(notification), f'Test Category - Test Message')


class NotificationListViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test data for the Notification model
        user = User.objects.create(name='Test User', email='test@example.com')
        notification_type = NotificationType.objects.create(name='Test Type')
        Notification.objects.create(category='Test Category', message='Test Message', user=user, notification_type=notification_type)

    def test_list_notifications(self):
        url = reverse('notification-list')
        response = self.client.get(url)
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)