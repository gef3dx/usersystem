from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from tinymce.widgets import TinyMCE


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Введите действительный адрес электронной почты, иначе письмо с активацией акаунта не дойдет', required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'phone', 'first_name', 'last_name',   'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Логин или Email")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}), label="Пароль")

    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), label="Вы не робот?")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'thread'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'image', 'description']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), label="Вы не робот?")