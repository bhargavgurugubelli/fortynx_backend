from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="services/")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
