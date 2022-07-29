from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
#from django_google_maps import widgets as map_widgets
#from django_google_maps import fields as map_fields

#class RentalAdmin(admin.ModelAdmin):
 #   formfield_overrides = {
  #      map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
   # }
class Useradmin(UserAdmin):
  fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'tel','adresse','codePostal','photos'
                ),
            },
        ),
    )

   

admin.site.register(User,Useradmin)
admin.site.register(Contact)
admin.site.register(Produit)
admin.site.register(Entrepot)
admin.site.register(Bureau)
admin.site.register(LocalCommercial)
admin.site.register(Terrain)
admin.site.register(Surface)
admin.site.register(GED)
admin.site.register(Transfert)
admin.site.register(Photo)
admin.site.register(Estimation)
admin.site.register(Offre)
admin.site.register(Demande)
admin.site.register(Mandat)

# Register your models here.
