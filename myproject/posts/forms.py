from django import forms
from . import models

class CreatPost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug']