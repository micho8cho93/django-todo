from django import forms
from .models import TodoItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'due_date', 'is_completed']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }