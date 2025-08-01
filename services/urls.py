from django.urls import path
from .views import ServiceListAPIView, ServiceDetailAPIView, ServiceCategoryListAPIView

urlpatterns = [
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('services/<slug:slug>/', ServiceDetailAPIView.as_view(), name='service-detail'),
    path('categories/', ServiceCategoryListAPIView.as_view(), name='category-list'),
]
