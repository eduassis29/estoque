from django.forms import ModelForm, TextInput, Select
from .models import Saidas

class SaidaForm(ModelForm):
    class Meta:
        model = Saidas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'quantidade': TextInput(attrs={'class': 'input'}),
            'preco': TextInput(attrs={'class': 'input'}),
            'produto': Select(attrs={'class': 'select'}),
        }
