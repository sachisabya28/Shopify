from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices
# Create your views here.

def index(request):
    listing = Listing.objects.order_by('-lis_date').filter(is_published = True)
    context = {
        'listings' : listing, 
        'bedroom_choices' : bedroom_choices, 
        'price_choices' : price_choices,
        'state_choices' : state_choices
        }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('hire_date')
    #realtor MVP
    realtor_mvp = Realtor.objects.all().filter(is_mvp = True)
    context = {
       'realtors' : realtors,
       'realtor_mvp' : realtor_mvp,
    }
    return render(request, 'pages/about.html', context)
