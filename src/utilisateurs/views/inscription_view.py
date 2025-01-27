from django.views.generic import CreateView
from django.urls import reverse_lazy
from ..forms.inscription_form import InscriptionForm
from ..services.utilisateur_service import UtilisateurService

class InscriptionView(CreateView):
    form_class = InscriptionForm
    template_name = 'utilisateurs/inscription.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        UtilisateurService.creer_utilisateur(
            username=user.username,
            email=user.email,
            password=form.cleaned_data['password'],
            role=user.role
        )
        return super().form_valid(form)
