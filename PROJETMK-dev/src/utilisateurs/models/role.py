from django.db import models

class Role(models.Model):
    ROLES = (
        ('admin', 'Administrateur'),
        ('editeur', 'Éditeur'),
        ('lecteur', 'Lecteur')
    )
    
    nom = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.nom
