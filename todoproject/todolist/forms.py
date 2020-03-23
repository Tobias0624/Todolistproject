from  django import forms
from . models import Todo, Category

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'