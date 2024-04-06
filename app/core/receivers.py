from django.dispatch import receiver
from .models import notification_sent

@receiver(notification_sent)
def handle_notification(sender, **kwargs):
    category = kwargs['category']
    message = kwargs['message']
    user_id = kwargs['user_id']

    # Handle the notification (e.g., send SMS, email, push notification)
    print(f"Notification sent to user {user_id}: Category - {category}, Message - {message}")
