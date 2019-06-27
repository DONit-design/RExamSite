from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm, \
    PasswordChangeForm
from django.forms import TextInput, Select, EmailInput
from fontawesome_5 import Icon
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from Accounts.models import RExamUserModel


class UserCreateForm(UserCreationForm):
    ReCaptcha = ReCaptchaField(ReCaptchaWidget(), label='', error_messages={'required': 'Каптча не пройдена!'})
    password1 = forms.CharField(label=Icon('key', 'fas').as_html(),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label=Icon('key', 'fas').as_html(),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    username = forms.RegexField(label=Icon('user', 'far').as_html(), max_length=30,
                                regex=r'[a-zA-Z0-9]+',
                                error_messages={
                                    'invalid': 'Только латинские символы и цифры!'},
                                widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))

    class Meta(UserCreationForm.Meta):
        model = RExamUserModel
        fields = (
            'username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'middle_name',
            'study_group')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'middle_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество'}),
            'study_group': Select(attrs={'class': 'form-control', 'placeholder': 'Группа'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail'}),
        }
        labels = {
            'first_name': Icon('address-card', 'far').as_html(),
            'last_name': Icon('address-card', 'far').as_html(),
            'middle_name': Icon('address-card', 'far').as_html(),
            'study_group': Icon('users', 'fas').as_html(),
            'email': Icon('envelope', 'far').as_html(),
        }


class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
                             label=Icon('user', 'far').as_html())
    password = forms.CharField(label=Icon('key', 'fas').as_html(),
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    ReCaptcha = ReCaptchaField(ReCaptchaWidget(), label='', error_messages={'required': 'Каптча не пройдена!'})


class UserProfileForm(UserChangeForm):
    password = None
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин', 'readonly': True}),
        label=Icon('user', 'far').as_html())
    ReCaptcha = ReCaptchaField(ReCaptchaWidget(), label='', error_messages={'required': 'Каптча не пройдена!'})

    class Meta:
        model = RExamUserModel
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name',
                  'study_group', 'ReCaptcha')
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'middle_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество', }),
            'study_group': Select(attrs={'class': 'form-control', 'placeholder': 'Группа'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-Mail'}),
        }
        labels = {
            'first_name': Icon('address-card', 'far').as_html(),
            'last_name': Icon('address-card', 'far').as_html(),
            'middle_name': Icon('address-card', 'far').as_html(),
            'study_group': Icon('users', 'fas').as_html(),
            'email': Icon('envelope', 'far').as_html(),
        }


class ChangePasswordForm(PasswordChangeForm):
    ReCaptcha = ReCaptchaField(ReCaptchaWidget(), label='', error_messages={'required': 'Каптча не пройдена!'})
    new_password1 = forms.CharField(label=Icon('key', 'fas').as_html(),
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Введите новый пароль'}))
    new_password2 = forms.CharField(label=Icon('key', 'fas').as_html(),
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Повторите новый пароль'}))
    old_password = forms.CharField(label=Icon('key', 'fas').as_html(),
                                   widget=forms.PasswordInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Введите старый пароль'}))
