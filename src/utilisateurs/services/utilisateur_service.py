from ..models import Utilisateur

class UtilisateurService:
    @staticmethod
    def creer_utilisateur(username, email, password, role):
        utilisateur = Utilisateur.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )
        return utilisateur

    @staticmethod
    def verifier_role(utilisateur, role_requis):
        return utilisateur.role == role_requis
