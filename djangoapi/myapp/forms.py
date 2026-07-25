from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    captcha = CaptchaField()
    
class RegistrationForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=50,
        widget=forms.TextInput(attrs={
            'class':'input',
            'placeholder':'Username kiriting'

        })
    )    

    password=forms.CharField(
        label="Parol",
        min_length=8,
        widget=forms.PasswordInput(attrs={
            'class':'input',
            'placeholder':'Kamida 8 ta belgi'

        }),
        error_messages={
            'min_length':'Parol kamida 8 ta belgidan iborat bolishi merak '

        }

    )