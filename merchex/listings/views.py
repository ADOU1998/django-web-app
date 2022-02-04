from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band # Importation de la BD
from listings.models import Listing

# Create your views here.
def hello(request):
    # Requette pour afficher touts les champs dans band
    bands = Band.objects.all()
    return render(request, 'brands/hello.html', {'bands': bands})

# fonction a propos
def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons !</p>')

# fonction listings
def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', {'listings': listings})

# fonction contact
def contacts(request):
    return HttpResponse('<h1>Contactez-nous !</h1>')