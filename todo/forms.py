from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    """Use model Todo in TodoForm"""
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
