from django.shortcuts import render

# Create your views here.

# Added by dev after this

def index(request):
    """View funciton for index page."""

    template = 'base/index.html'
    context = {}

    return render(request, template, context)

