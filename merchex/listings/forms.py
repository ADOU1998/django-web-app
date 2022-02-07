from dataclasses import field
import imp
from django import forms
from listings.models import Band, Listing
from django.core.validators import MaxValueValidator, MinValueValidator

# Formulaire de contact
class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

# Formulaire de goupe herite de sa classe
class BandForm(forms.ModelForm):
   class Meta:
      model = Band
      # fields = '__all__' # Afficher tout les champs
      exclude = ('active', 'official_homepage') # pour exlure certains champs

# Formulaire de l'annonce
class ListingForm(forms.ModelForm):
   class Meta:
      model = Listing
      fields = '__all__'
