from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Dynamic form creation"""
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')
