from django import forms
from django.contrib.auth.models import User
from .models import Profile  # À créer si vous souhaitez stocker des informations supplémentaires
from django.core.exceptions import ValidationError


# Formulaire pour modifier les informations du profil
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # Ajoutez d'autres champs si nécessaire

    # Si vous souhaitez gérer une photo de profil, ajoutez un champ pour cela.
    profile_picture = forms.ImageField(required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise ValidationError("Ce nom d'utilisateur est déjà pris.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("Cet email est déjà utilisé.")
        return email


# Formulaire pour gérer les informations de carte
class CardForm(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': '1234 5678 9101 1121'}))
    expiry_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/AA'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'placeholder': '123'}))


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture']  # Ajoutez ici le champ pour la photo

    profile_picture = forms.ImageField(required=False)
