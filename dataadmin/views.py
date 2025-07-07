
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404

# Create your views here.

def can_proceed(request, role):
    """
    Check if user has necessary role and is allowed to proceed
    """
    username = request.user
    user = get_object_or_404(User, username=username)

    if not user.groups.filter(name=role).exists():
        raise PermissionDenied('Permission denied')

    return True


@login_required
def index(request):
    can_proceed(request, 'DataAdmin')

    template = 'dataadmin/index.html'
    context = {}

    return render(request, template, context)


@login_required
def search(request):
    """
    This view is used to search for items
    """
    can_proceed(request, 'DataAdmin')

    template = 'dataadmin/search_result.html'
    search_criteria = request.POST.get('q')
    context = {
        'search_criteria': search_criteria,
        'search_result': 'Search result is none of your business'
    }
    return render(request, template, context)
