from django.contrib import admin
from GestionElectro.models import   Fournisseur, Paiement, PetitProduit, Produit,Client

#Register your models here.

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin): 
   list_display = ("nom","prix") 
   list_editable =("nom",)
   list_display_links = ("prix",)
   search_fields = ("nom",)
   list_filter = ("marque",)
   list_per_page= 4
@admin.register(PetitProduit)
class PetitProduitAdmin(admin.ModelAdmin):
   list_display = ("nom","reference") 
   list_editable =("reference",)
   list_display_links = ("nom",)
   search_fields = ("marque",)
   list_filter = ("marque",)
   list_per_page= 4
@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
   list_display = ("nomF",) 

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
   list_display = ("nom",) 
 
@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
   list_display = ("code",)
