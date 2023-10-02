
from django import forms
from .models import Category, Author, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'categories']
        