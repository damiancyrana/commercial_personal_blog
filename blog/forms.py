from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Dynamic form creation"""
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')


class SearchForm(forms.Form):
    """PostgreSQL search view"""
    query = forms.CharField()
