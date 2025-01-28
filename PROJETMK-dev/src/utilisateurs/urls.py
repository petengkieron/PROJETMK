from django.urls import path 
from .views.inscription_view import inscription 
from .views.connexion_view import connexion 

urlpatterns = [ 
   path('inscription/', inscription, name='inscription'), 
   path('connexion/', connexion, name='connexion'), 
]
