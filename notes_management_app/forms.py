from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title', 'class': 'border focus:outline-none focus:ring-2 focus:ring-blue-300 rounded p-2 w-full'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter the Description', 'class': 'border focus:outline-none focus:ring-2 focus:ring-blue-300 rounded p-2 w-full h-24'}),
        }

