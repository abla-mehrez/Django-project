from django.urls import path

from .views import contactView,successView


urlpatterns = [
path("",contactView),
path("s",successView),
]
