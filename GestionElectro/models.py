from django.db import models
from django.forms import IntegerField



# Create your models here.
#class produit
class Produit(models.Model):
    nom=models.CharField(max_length=100) 
    marqueType=models.TextChoices('marqueType', 'LG SAMSUNG MontBlanc Condor BIOLUX WHIRLPOOL COALA  ')
    marque=models.CharField(blank=True,choices=marqueType.choices,max_length=20)
    reference=models.CharField(max_length=50,blank=True) 
    prix=models.FloatField(default=0)
    image=models.ImageField(upload_to='GestionElectro/fichier/images')
    description=models.TextField(blank=True)
    #lezemny na3mel dossier essmou electro lel les images
    def __str__(self):
        return self.nom
  
#class produit

#class petitProduit
class PetitProduit(Produit,models.Model):
    couleur=models.CharField(max_length=100,blank=True)
    capacite=models.FloatField(default=0)
    puissance=models.FloatField(default=0)
    fonctionAntiGoutte=models.CharField(max_length=100,blank=True)
    Carafeetentonnoirlavables=models.CharField(max_length=100,blank=True)
    Dispositifantichauffageàsec=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.nom + self.reference
#class petitProduit
    

#classclient
class Client(models.Model):
    nom=models.CharField(max_length=100) 
    prenom=models.CharField(max_length=100)
    adresse:models.CharField(max_length=100)
    numTel=models.BigIntegerField(default=0)
    def __str__(self):
        return self.nom + self.prenom
#classclient

#classfournisseur
class Fournisseur(models.Model):
    nomF=models.CharField(max_length=100) 
    prenomF=models.CharField(max_length=100)
    adresseF:models.CharField(max_length=100)
    numTelF=models.BigIntegerField(default=0)
    def __str__(self):
        return self.nomF + self.prenomF
#classfournisseur

#classcontact
class Contact(models.Model):
    firstname=models.CharField(max_length=100, blank=False)
    lastname=models.CharField(max_length=100,  blank=False)
    Email=models.EmailField(  blank=False)
    msg=models.TextField(  blank=False)
#classcontact

total=IntegerField

class Paiement(models.Model):
    code=models.CharField(max_length=100)
    date=models.DateTimeField(null=True)
    product=models.OneToOneField(Produit,on_delete=models.SET_NULL,null=True)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,blank=True)  
    quantité=models.IntegerField(default=0)
    prixTotal= models.FloatField(default=0)
   

    def calc_total(self):
       pass
       
    def save(self):
       total= self.product.prix *self.quantité
       self.prixTotal = total
       super(Paiement, self).save()


       
    def __str__(self):
        return self.code
  
