from rest_framework import generics
from .models import Service, ServiceCategory
from .serializers import ServiceSerializer, ServiceCategorySerializer


# ✅ List all services with their features and category
class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# ✅ Get a single service by its slug
class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'  # Enables access like /api/services/your-service-slug/


# ✅ List all service categories
class ServiceCategoryListAPIView(generics.ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
