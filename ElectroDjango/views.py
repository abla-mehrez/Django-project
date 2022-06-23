from django.shortcuts import render

from GestionElectro.models import PetitProduit, Produit


def home (request):
    # result=Produit.objects.all()
    # context={'produit':result}
    return render(request,'ElectroDjango/home.html')