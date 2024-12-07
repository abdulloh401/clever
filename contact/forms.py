from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your  message'}),
        }
