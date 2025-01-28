from django.contrib.auth import authenticate, login
from ..models.utilisateur import Utilisateur
from ..models.role import Role 
class UtilisateurService:
    
    @staticmethod
    def creer_utilisateur(username, email, password, role_nom):
        role, created = Role.objects.get_or_create(nom=role_nom)
        utilisateur = Utilisateur.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
        )
        return utilisateur

    @staticmethod
    def connecter_utilisateur(request, username, password):
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return user
        return None
