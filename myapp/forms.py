from django import forms
from .models import User
from .models import UploadedImage

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['id', 'password', 'blood_sugar_target', 'height', 'weight']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']