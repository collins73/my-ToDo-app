from django import forms
from .models import ToDoList

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ["item", "completed"]
