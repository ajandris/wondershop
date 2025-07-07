
from django.urls import path

from .views import index, search

urlpatterns = [
    path('search/', search, name='da-search'),
    path('', index, name='data-admin-home'),
]
