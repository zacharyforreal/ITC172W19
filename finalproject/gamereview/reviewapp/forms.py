from django import forms
from .models import Game, GameType, Review

class GameForm(forms.ModelForm):
    class Meta:
        model=Game
        fields='__all__'