
from django.urls import path

from .views import index, search

urlpatterns = [
    path('search/', search, name='search'),
    path('', index, name='home'),
]
