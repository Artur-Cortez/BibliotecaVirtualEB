from django import forms

class LoginForm(forms.Form):
           
    login = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'id': 'username',
            'name': 'login',
            'placeholder': 'Username',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'placeholder': 'Senha',
            'class': 'form-control'
        })
    )