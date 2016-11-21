from django import forms
from .models import Post
from django.utils.translation import ugettext as _


class PostForm(forms.ModelForm):
    text = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'postText'}))

    class Meta:
        model = Post
        fields = ['text']
