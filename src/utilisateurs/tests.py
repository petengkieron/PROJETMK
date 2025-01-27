from django.test import TestCase
from django.urls import reverse
from .models import Utilisateur

class UtilisateurTests(TestCase):
    def test_inscription(self):
        response = self.client.post(reverse('inscription'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass123',
            'role': 'LECTEUR'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après inscription
        self.assertTrue(Utilisateur.objects.filter(username='testuser').exists())

    def test_connexion(self):
        Utilisateur.objects.create_user(username='testuser', password='testpass123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après connexion

    def test_role_verification(self):
        user = Utilisateur.objects.create_user(username='testuser', password='testpass123', role='AUTEUR')
        self.client.login(username='testuser', password='testpass123')
        # Ajoutez ici un test pour vérifier l'accès à une vue protégée par rôle
