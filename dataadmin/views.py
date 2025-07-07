from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def index(request):
    template = 'dataadmin/index.html'
    context = {}

    return render(request, template, context)


@login_required
def search(request):
    """
    This view is used to search for items
    """
    template = 'dataadmin/search_result.html'
    search_criteria = request.POST.get('q')
    context = {
        'search_criteria': search_criteria,
        'search_result': 'Search result is none of your business'
    }
    return render(request, template, context)
