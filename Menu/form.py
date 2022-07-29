from dataclasses import field
from operator import mod
from pyexpat import model
from django.forms import ModelForm
from .models import *
from django import forms
class formC(ModelForm):
    class Meta:
     model = Contact
     fields = '__all__'

class Produitform(ModelForm):
    class Meta: 
     model = Produit
     fields = '__all__'

class Entrepotform(ModelForm):
    class Meta:
     model = Entrepot
     fields = '__all__'
class SurfaceForm(ModelForm):
    class Meta:
        model = Surface
        fields = '__all__'
class LocalcomForm(ModelForm):
    class Meta:
        model = LocalCommercial
        fields = '__all__'
class TerrainForm(ModelForm):
    class Meta:
        model = Terrain
        fields = '__all__'
class PhotosForm(ModelForm):
    class Meta:
       model = Photo
       fields = '__all__'
       widgets = {
            
            'image': forms.FileInput(attrs= { 'onchange':'loadFile(event)'  }),
            
            }
class DemandeForm(ModelForm):
    class Meta:
        model = Demande
        fields = '__all__'

class MandatForm(forms.ModelForm):
    class Meta:
        model = Mandat
        fields = '__all__'

class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = '__all__'

class AchatForm(forms.ModelForm):
    class Meta:
        model = Achat
        fields = '__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class EstimationForm(ModelForm):
   class Meta:
      model = Estimation
      fields = '__all__'

class GedForm(ModelForm):
    class Meta:
        model = GED
        fields = '__all__'
