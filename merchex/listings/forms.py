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

class BandForm(forms.ModelForm):
   class Meta:
      model = Band
      fields = '__all__'
