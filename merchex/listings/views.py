from crypt import methods
import re
from xml.etree.ElementTree import fromstringlist
from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.models import Band # Importation de la table Band
from listings.models import Listing
from listings.forms import ContactUsForm , BandForm , ListingForm 
from django.core.mail import send_mail # Importation pour envoyer un mail

# Create your views here.
# ---- GROUPE --------
def band_list(request):
    bands = Band.objects.all() # Requette pour afficher touts les champs dans band
    return render(request, 'bands/band_list.html', {'bands': bands})

# Vue id band en argument pour afficher élément de la band dans le url
def band_detail(request, id):
    band = Band.objects.get(id=id) # Obtenir le band avec son id
    return render(request, 'bands/band_detail.html', {'band': band}) # Nous passons l'id au modèle

# Créer un formulaire : Band --> groupe
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle <<Band>> et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'bands/band_create.html', {'form': form})

# Mise à jour d'un groupe via l'id
def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # Mettre à jour le groupe existant dans la base de données
            form.save()
            # Rédiriger vers la page détaillé du groupe
            return redirect('band-list', band.id)
    else:
        form = BandForm(instance=band) # on pré-remplir le foemulaire avec un groupe existant

    return render(request, 'bands/band_update.html', {'form': form})

# Supprimer un groupe
def band_delete(request, id):
    band = Band.objects.get(id=id) # nécessaire pour GET et pour POST

    if request.method == 'POST':
        band.delete() # Supprimer le groupe de la BD
        return redirect('band-list')
    return render(request, 'bands/band_delete.html', {'band': band})

# ---- FIN GROUPE --------

# fonction a propos
def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons !</p>')

# ---- ANNONCE --------
# Formulaire de création de l"annonce
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})

# fonction listings
def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 
            'listings/listing_list.html', 
            {'listings': listings})

def listing_detail(request, id):
    listings = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', {'listings': listings})

# Mise à jour d'un groupe via l'id
def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # Mettre à jour de l'annonce existant dans la base de données
            form.save()
            # Rédiriger vers la page détaillé de l'annonce
            return redirect('listing-list', listing.id)
    else:
        form = ListingForm(instance=listing) # on pré-remplir le foemulaire avec un groupe existant

    return render(request, 'listings/listing_update.html', {'form': form})

# ---- FIN ANNONCE --------

# fonction contact
def contact(request):
 # ...nous pouvons supprimer les déclarations de journalisation qui étaient ici...
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)  # ajout d’un nouveau formulaire ici

        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["name"] or "anonyme"} via le formulaire de contact Merchex',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent') # Rédirige vers une nouvelle page
    
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
       form = ContactUsForm(request.POST) 
    return render(request, 'listings/contact.html', {'form': form})  # passe ce formulaire au gabarit