from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

from .models import MenuCategory, MenuItem, Review, ContactMessage
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse


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

class ContactMessageCreate(CreateView):
    """View class for creating contact message."""

    template_name = 'base/contact.html'
    model = ContactMessage
    fields = [
        'sender_name',
        'sender_email',
        'message',
    ]

    def get_success_url(self):
        """Override success url."""

        return reverse('base-contact-success')

def contactMessageSuccess(request):
    """View function for contact message success."""

    template = 'base/contact_success.html'
    context = {}

    return render(request, template, context)

class ReviewListView(generic.ListView):
    """View class for review list."""

    model = Review

class ReviewCreate(CreateView):
    """View class for review create."""

    template_name = 'base/review_create.html'
    model = Review
    fields = '__all__'

    def get_success_url(self):
        """Overwrite success url."""

        return reverse('base-review-success')

def reviewSuccess(request):
    """View function for review success."""

    template = 'base/review_success.html'
    context = {}

    return render(request, template, context)

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

