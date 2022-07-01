from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation, validators
from django.core import validators

from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Підтвердження паролю',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_('Введіть пароль для підтвердження'),
    )
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

        
        labels = {
            'first_name': "Ім'я",
            'email': 'Email',
            'username': 'Нікнейм',
        }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    profile_image = forms.FileField(label='Зображення профілю', widget=forms.FileInput,validators=[validators.validate_image_file_extension], required=False)
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'bio', 'short_intro', 'profile_image',
        'social_instagram', 'social_facebook', 'social_linkedin', 'social_viber', 'social_telegram']
        labels = {
            'name': "Ім'я",
            'email': 'Email',
            'username': 'Нікнейм',
            'bio': 'Опис',
            'short_intro': 'Короткий опис',
            'profile_image': 'Зображення профілю',
            'social_instagram': 'Instagram',
            'social_facebook': 'Facebook',
            'social_linkedin': 'Linkedin',
            'social_viber': 'Viber',
            'social_telegram': 'Telegram'
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})