from django.urls import path
from .views import contact_submit

from contact.views import list_media 

urlpatterns = [
    path('', contact_submit, name='contact-submit'),
    path("debug-media/", list_media)
]
