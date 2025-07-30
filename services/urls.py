from django.urls import path
from .views import ServiceDetailView

urlpatterns = [
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
]
