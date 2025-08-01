from rest_framework import serializers
from .models import ServiceCategory, Service, ServiceFeature

class ServiceFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeature
        fields = ['text']

class ServiceSerializer(serializers.ModelSerializer):
    features = ServiceFeatureSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Service
        fields = ['id', 'title', 'slug', 'description', 'icon', 'image', 'category', 'features']

class ServiceCategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'services']
