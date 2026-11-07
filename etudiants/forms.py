
from django import forms
from .models import Etudiant


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant

        fields = [
            'nom',
            'prenom',
            'programme',
            'remarque',
        ]

        widgets = {
            'nom': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nom de l’étudiant',
                }
            ),
            'prenom': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Prénom de l’étudiant',
                }
            ),
            'programme': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex. Informatique',
                }
            ),
            'remarque': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Remarque facultative',
                }
            ),
        }
