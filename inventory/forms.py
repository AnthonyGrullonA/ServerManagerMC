# forms.py

from django import forms
from .models import Inventory, CellConfiguration

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'description']

class CellConfigurationForm(forms.ModelForm):
    class Meta:
        model = CellConfiguration
        fields = ['label', 'cell_type']
