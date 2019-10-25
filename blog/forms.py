from django import forms

from .models import Post_Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post_Comment
        fields = ('user_name', 'comment')
