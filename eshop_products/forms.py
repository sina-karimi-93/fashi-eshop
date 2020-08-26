from .models import Comment
from django import forms
from django.core import validators


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Your Comment'}),
        }

# class CommentForm(forms.Form):
#     name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Name'}),
#         label='Name',
#         validators=[
#             validators.MinLengthValidator(limit_value=10, message='Too Much Charracters')
#         ]
#     )
#
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Email'})
#     )
#
#     body = forms.CharField(
#         widget=forms.Textarea(attrs={'placeholder': 'Your Comment'})
#     )
