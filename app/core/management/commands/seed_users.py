# myapp/management/commands/seed_users.py
from django.core.management.base import BaseCommand
import faker

import random

from  core.models  import Category, NotificationType, User


class Command(BaseCommand):
    help = 'Seeds the database with fake users'

    def handle(self, *args, **kwargs):
        fake = faker.Faker()
        categories = Category.objects.all()
        notification_types = NotificationType.objects.all()

        if not categories or not notification_types:
            self.stdout.write(self.style.ERROR("No categories or notification types found in the database. Please ensure you have some categories and notification types created."))
            return

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
