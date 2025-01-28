# src/utilisateurs/models/utilisateur.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from .role import Role

class Utilisateur(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
