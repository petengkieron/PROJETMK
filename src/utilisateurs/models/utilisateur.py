from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrateur'),
        ('AUTEUR', 'Auteur'),
        ('LECTEUR', 'Lecteur'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='LECTEUR')

    def __str__(self):
        return self.username
