from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    avatar = forms.ImageField(required=False)  # Додайте поле для аватарки

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        exclude = ['password']
        fields = ('first_name', 'last_name', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')