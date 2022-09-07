from .models import Word
from django.forms import ModelForm, TextInput, Textarea


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ["name", "definition"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-controll',
                'placeholder': "Введите название",
            }),
            "definition": Textarea(attrs={
                'class': 'form-controll',
                'placeholder': "Введите определение",
            }),
        }
