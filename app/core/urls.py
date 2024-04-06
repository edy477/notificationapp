from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserListView, NotificationViewSet
from . import views
app_name = "core"
# notification_list = UserViewSet.as_view({'get':'list', 'post':'create'})
# notifications_actions =  NotificationView.as_view({'get':'list', 'post':'create'})

notifications_actions = NotificationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),

    path("notifications", notifications_actions, name='notifications-actions'),
]


# urlpatterns = [
#     path("", notification_list, name='notification-list'),
#     path("notifications", notifications_actions, name='notifications-actions'),
# ]

# app_name = "core"
#
# urlpatterns = [
#     path("", views.index, name="index"),
# ]
