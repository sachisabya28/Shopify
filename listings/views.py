from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import bedroom_choices, price_choices, state_choices

# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-lis_date').filter(is_published = True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings}

    return render(request, 'listings/listings.html', context)


def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk =listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

    
def search(request):
    queryset_list  =  Listing.objects.order_by('-lis_date')
    
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(description__iexact = keywords)

    if 'state' in request.GET:
        keywords = request.GET['state']
        if keywords:
            queryset_list = queryset_list.filter(description__iexact = keywords)

    if 'bedrooms' in request.GET:
        keywords = request.GET['bedrooms']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)

    context = {
        'listings' : queryset_list,
        'bedroom_choices' : bedroom_choices, 
        'price_choices' : price_choices,
        'state_choices' : state_choices
        }
    return render(request, 'listings/search.html', context)

