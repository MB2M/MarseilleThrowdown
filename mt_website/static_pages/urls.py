from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import Index, ContactEmail, WodOne, WodTwo, WodThree

app_name = 'static_pages'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact-email', ContactEmail.as_view(), name='contact_email'),
    path('wod1', WodOne.as_view(), name='wod_one'),
    path('wod2', WodTwo.as_view(), name='wod_two'),
    path('wod3', WodThree.as_view(), name='wod_three'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
