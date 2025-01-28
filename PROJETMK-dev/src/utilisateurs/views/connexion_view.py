from django.shortcuts import render, redirect
from ..services.utilisateur_service import UtilisateurService
from ..forms.connexion_form import ConnexionForm

def connexion(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UtilisateurService.connecter_utilisateur(request, username, password)
            if user:
                return redirect('accueil')  # Rediriger vers une page d'accueil ou tableau de bord.
    
    else:
        form = ConnexionForm()
    
    return render(request, "utilisateurs/connexion.html", {"form": form})
