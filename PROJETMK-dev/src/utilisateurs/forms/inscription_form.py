# src/utilisateurs/forms/inscription_form.py
from django import forms

class InscriptionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=150)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label="Confirmation du mot de passe", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        
        return cleaned_data
