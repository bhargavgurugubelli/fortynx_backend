from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Creates a default admin user"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = "fortynx"
        password = "Forty@79012"
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created with password '{password}'"))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists"))
