from django.urls import path
from .views.inscription_view import InscriptionView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('connexion/', LoginView.as_view(template_name='utilisateurs/connexion.html'), name='login'),
    path('deconnexion/', LogoutView.as_view(), name='logout'),
]
