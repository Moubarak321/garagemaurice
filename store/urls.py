from django.urls import path
from . import views
urlpatterns = [
    path('vehicules/', views.vehicules , name = "vehicules" ),  
    path('a-propos/', views.a_propos , name = "a-propos" ),  
    path('voiture/<str:slug>', views.voiture , name = "voiture" ),  
    path('reserver', views.reserver , name = "reserver" ),  
    path('services', views.service , name = "service" ),  
    path('contact', views.contact , name = "contact" ),  
] 
