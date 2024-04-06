from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, generics
from rest_framework.views import APIView

from .models import  User
from .serializers import UserSerializer, NotificationSerializer

from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Notification,notification_created

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        # Add any custom logic here before returning the response
        return super().list(request, *args, **kwargs)
class NotificationViewSet(viewsets.ViewSet):
    serializer_class = NotificationSerializer
    def create(self, request, format=None):
        category = request.data.get('category')
        message = request.data.get('message')

        if category is None or message is None:
            return Response({"error": "Category and message are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Get all users subscribed to the category
        users_subscribed = User.objects.filter(subscribed_categories__name=category)

        if not users_subscribed.exists():
            return Response({"error": "No users subscribed to this category"}, status=status.HTTP_400_BAD_REQUEST)

        for user in users_subscribed:
            # Create a notification object for each user
            notification = Notification.objects.create(
                category=category,
                message=message,
                timestamp=datetime.now(),
                user=user
            )

            # Emit the notification_created signal
            notification_created.send(sender=None, notification=notification)

        return Response({"message": f"Notifications created and sent to {users_subscribed.count()} users"}, status=status.HTTP_201_CREATED)

    def list(self, request, format=None):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications,many=True)
        return Response(serializer.data)