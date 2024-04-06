# myapp/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from faker import Faker
from core.models import User, Category, NotificationType
import random

class Command(BaseCommand):
    help = 'Seeds the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Seed categories
        categories = ['Sports', 'Finance', 'Movies']
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)
            self.stdout.write(self.style.SUCCESS(f'Successfully created category: {category_name}'))

        # Seed notification types
        notification_types = ['SMS', 'Email', 'Push Notification']
        for notification_type_name in notification_types:
            NotificationType.objects.get_or_create(name=notification_type_name)
            self.stdout.write(self.style.SUCCESS(f'Successfully created notification type: {notification_type_name}'))

        # Seed users
        categories = Category.objects.all()
        notification_types = NotificationType.objects.all()

        for _ in range(10):
            user = User.objects.create(
                user_id=fake.uuid4(),
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                # Assuming other fields are optional or have defaults
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.name}'))

            # Randomly subscribe the user to categories if available
            if categories.exists():
                user.subscribed_categories.add(*random.sample(list(categories), random.randint(1, len(categories))))

            # Randomly assign notification channels to the user if available
            if notification_types.exists():
                user.notification_channels.add(*random.sample(list(notification_types), random.randint(1, len(notification_types))))

            self.stdout.write(self.style.SUCCESS(f'Subscribed categories for {user.name}: {", ".join(user.subscribed_categories.values_list("name", flat=True))}'))
            self.stdout.write(self.style.SUCCESS(f'Notification channels for {user.name}: {", ".join(user.notification_channels.values_list("name", flat=True))}'))
