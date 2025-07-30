from django.core.management.base import BaseCommand
from services.models import Service  # Change 'services' if your app name is different
from PIL import Image

class Command(BaseCommand):
    help = "Resize and compress existing service images"

    def handle(self, *args, **kwargs):
        services = Service.objects.all()
        for service in services:
            if service.image:
                img_path = service.image.path
                try:
                    img = Image.open(img_path)
                    max_size = (600, 400)
                    img.thumbnail(max_size)
                    img.save(img_path, format='JPEG', quality=80, optimize=True)
                    self.stdout.write(self.style.SUCCESS(f"Optimized: {img_path}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Failed: {img_path} | {e}"))
