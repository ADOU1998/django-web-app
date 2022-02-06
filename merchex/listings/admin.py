from csv import list_dialects
from django.contrib import admin

# Register your models here.
from listings.models import Band, Listing # importer le modele Brand et Listing

class BandAdmin(admin.ModelAdmin): # Insérer des lignes sur notre site admin
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year', 'type', 'band') # Ajout de band

# enregistrer le model sur notre site admin et nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Band, BandAdmin)

admin.site.register(Listing, ListingAdmin)
