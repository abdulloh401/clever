from django import forms
from course.models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your website'}),
        }
    