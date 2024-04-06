from rest_framework import serializers

from .models import User
from .models import Notification


# from .models import EmailNotification
# from .models import SMSNotification
# from .models import  PushNotification

# class EmailNotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  EmailNotification
#         fields = '__all__'
# class SMSNotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  SMSNotification
#         fields = '__all__'
#
# class PushNotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =  PushNotification
#         fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model= Notification
        fields = ['id', 'category', 'message', 'timestamp', 'user_name']  # Include user's name in the fields
 #"__all__"