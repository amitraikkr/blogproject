from django import forms
from .models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('author','title', 'text','post_pic')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.CharField(widget=CKEditorUploadingWidget()),
            
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder':'Email'
        }),required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Subject'
        }),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder':'Message'
        }), required=True)
    
