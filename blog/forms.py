from django import forms
from .models import Blog


class BlogForm(forms.Form):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'created_at', 'publication_sign', 'count_of_views']
