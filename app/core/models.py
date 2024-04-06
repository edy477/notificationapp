from django.db import models

# Create your models here.
from django.dispatch import Signal

# Define choices for MessageCategory enum
MESSAGE_CATEGORY_CHOICES = [
    ('SPORTS', 'Sports'),
    ('FINANCE', 'Finance'),
    ('MOVIES', 'Movies'),
]

# Define choices for NotificationType enum
NOTIFICATION_TYPE_CHOICES = [
    ('SMS', 'SMS'),
    ('EMAIL', 'Email'),
    ('PUSH_NOTIFICATION', 'Push Notification'),
]


notification_created  = Signal()

class User(models.Model):
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    subscribed_categories = models.ManyToManyField('Category', related_name='subscribers')
    notification_channels = models.ManyToManyField('NotificationType')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, choices=MESSAGE_CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class NotificationType(models.Model):
    name = models.CharField(max_length=50, choices=NOTIFICATION_TYPE_CHOICES)

    def __str__(self):
        return self.name

class Notification(models.Model):
    category = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.category} - {self.timestamp}"


