from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    """
    This view is for page's home page
    """
    return render(request, 'main/index.html')

@csrf_exempt
def search(request):
    """
    This view is used to search for items
    """
    search_criteria = request.GET.get('q')
    context = {
        'search_criteria': search_criteria
    }

    return render(request, template_name='main/search_result.html', context=context)

