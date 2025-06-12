from django import forms
from portfolioapp.models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control small-input',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control small-input',
                'placeholder': 'Enter your email'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control small-input',
                'placeholder': 'Write a short description',
                'rows': 4
            }),
            'userpic': forms.ClearableFileInput(attrs={
                'class': 'form-control small-input'
            })
        }
