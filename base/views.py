from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from .models import MenuCategory, MenuItem, Review
from django.views import generic

from .forms import FoodSearchForm
from django.http import HttpResponseRedirect

def index(request):
    """View function for index."""

    template = 'base/index.html'
    context = {}

    return render(request, template, context)

def contact(request):
    """View function for contact page."""

    template = 'base/contact.html'
    context = {}

    return render(request, template, context)

class ReviewListView(generic.ListView):
    """View class for review list."""

    model = Review

def reservation(request):
    """View function for reservation."""

    template = 'base/reservation.html'
    context = {}

    return render(request, template, context) 

def displayMenu(request):
    """View function for menu page."""

    template = 'base/menu.html'

    # Get the menu items from db
    menu_categories = MenuCategory.objects.all()
    context = {'menu_categories': menu_categories,}

    return render(request, template, context) 

def order(request):
    """View function for menu page."""

    template = 'base/order.html'

    # if post then process
    if request.method == 'POST':
        # create form
        form = FoodSearchForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # process form.cleaned_data
            return HttpResponseRedirect('/base/')
    # else if GET
    else:
        form = FoodSearchForm()

    context = {
        'form': form,
    }

    return render(request, template, context) 

