from django.urls import path
from .views import home , contact , contact_create
urlpatterns = [
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('contacts/',contact_create,name='contact_create'),
    ]