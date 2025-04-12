from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'lotr-input'}),
            'description': forms.Textarea(attrs={'class': 'lotr-textarea'}),
            'completed': forms.CheckboxInput(attrs={'class': 'lotr-checkbox'}),
        } 