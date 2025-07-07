"""
Module: errors.py
Description: custom error page handling
"""
from django.shortcuts import render


def custom_404(request, exception):
    """
    Custom 404 (Page not found) error page
    """
    return render(request, 'error/404.html', status=404)


def custom_403(request, exception):
    """
    Custom 403 (Permission denied) error page
    """
    return render(request, 'error/403.html', status=403)
