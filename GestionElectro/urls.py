from django.urls import include, path

from GestionElectro.views import  DetProd, SignUpView, apphome, controleform1, controleform2, controleform3
urlpatterns = [
path("apphome",apphome, name='apphome'),
path("<int:prod_id>/",DetProd,name='details'),
#path("cart/<object_id>",AddToCart, name='addToCart'),
#path("apphome<str:marques>/",apphome, name='apphome'),
path("form1",controleform1, name='contact'),
path("form2",controleform2),
path("form3",controleform3),
path('signup/', SignUpView.as_view(), name='signup'),
path('accounts/', include('django.contrib.auth.urls'), name='login'),
]
