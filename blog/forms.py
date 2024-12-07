from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('blog', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}),
        }
