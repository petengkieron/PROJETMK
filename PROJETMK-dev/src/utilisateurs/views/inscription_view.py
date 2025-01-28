# src/utilisateurs/views/inscription_view.py
from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms.inscription_form import InscriptionForm

def inscription(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # Logique pour créer l'utilisateur ici
            messages.success(request, "Inscription réussie.")
            return redirect('connexion')  # Redirige vers la page de connexion
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = InscriptionForm()
    
    return render(request, "utilisateurs/inscription.html", {"form": form})
