# models.py

from django.db import models
from django.utils.text import slugify

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)  # used for /service/slug
    description = models.TextField()
    icon = models.CharField(max_length=50)  # for frontend icon like ShoppingCart
    image = models.ImageField(upload_to='services/', null=True, blank=True)  # for detail page

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
