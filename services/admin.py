from django.contrib import admin
from .models import ServiceCategory, Service, ServiceFeature

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline]
