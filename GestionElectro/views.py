from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from GestionElectro.forms import contactform2

from .models import Contact, Produit

# Create your views here.
# def apphome(request):
#    if request.method == 'POST':
        
#      resultBymarqueLG=Produit.objects.filter(marque="LG")
#      appHomeDict={"marqueLG":resultBymarqueLG}
#      return render (request,'GestionElectro/apphome.html',appHomeDict)
        
#    else:
#      resultAppHome=Produit.objects.all()
#      appHomeDict={"ProductList":resultAppHome}
#      return render (request,'GestionElectro/apphome.html',appHomeDict)


def apphome(request):
 if request.method == 'POST':
        marques=request.POST.get('marque')
        print(marques)
        resultBymarque=Produit.objects.filter(marque=marques)
        print(resultBymarque)
        appHomeDict={"marque":resultBymarque}
        
        return render (request,'GestionElectro/apphome.html',appHomeDict)
 else:
         resultAppHome=Produit.objects.all()
         appHomeDict={"ProductList":resultAppHome}
         return render (request,'GestionElectro/apphome.html',appHomeDict)

def DetProd(request,prod_id):
     ProdById=Produit.objects.get(pk=prod_id)
     IDProd={"productbyid":ProdById}
     return render(request,'GestionElectro/detailProduit.html',IDProd)
"""  
def AddToCart(request, **kwrags):
    product=Produit.objects.filter(id=kwrags.get('product_id',"")).first()
"""


def controleform1(request):
    if request.method=='POST':
        f=request.POST['firstname']
        l=request.POST['lastname']
        e=request.POST['email']
        m=request.POST['message']
        c=Contact(firstname=f,lastname=l,Email=e,msg=m)
        c.save()
        return HttpResponse ('<h2> Data has been submitted </h2>')
    return render(request,'GestionElectro/apphome.html')


def controleform2(request):
    if request.method == 'POST':
        form = contactform2(request.POST)
        if form.is_valid():
            f = form.cleaned_data['firstname']
            l = form.cleaned_data['lastname']
            e = form.cleaned_data['Email']
            m = form.cleaned_data['msg']
            contact=Contact.objects.create(firstname=f,lastname=l,Email=e,msg=m)
            return HttpResponse('<h2> Data has been submitted </h2>')
    else:
      form = contactform2()

    return render(request,"GestionElectro/myform2.html",{'mycontactform2':form})


class contactform3(ModelForm):
    class Meta:
        model=Contact
        fields=('firstname','lastname','Email','msg')

def controleform3 (request):
    if request.method == 'POST': # S'il s'agit d'une requête POST
        form = contactform3(request.POST) # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont
#valides

            form.save()
            return HttpResponse(' <h2> Data has been submitted </h2>')
    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = contactform3() # Nous créons un formulaire vide
    return render(request,'GestionElectro/myform3.html',{'mycontactform3':form})
    #accounts:
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'