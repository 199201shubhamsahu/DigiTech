from django import forms
from .models import contact, transaction

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('name', 'email', 'query')

class transactionForm(forms.ModelForm):
    class Meta:
        model = transaction
        fields = ('username', 'quantity', 'lap_id')
