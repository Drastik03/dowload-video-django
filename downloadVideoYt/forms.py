from django import forms
from . models import VideoModel
class FormVideo(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = [
            'title',
            'videoLink',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title','placeholder': 'Write a title'}),
            'videoLink': forms.TextInput(attrs={'class': 'form-video', 'placeholder': 'Write a description'}),
        }