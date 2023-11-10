# Create a management command (e.g., create_user_profiles.py)
from django.core.management.base import BaseCommand
from events_app.models import UserProfile
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create UserProfile objects for users without one'

    def handle(self, *args, **options):
        users_without_profile = User.objects.filter(userprofile__isnull=True)
        for user in users_without_profile:
            UserProfile.objects.create(user=user)