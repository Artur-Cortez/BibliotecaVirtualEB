from django import forms

class SignupForm(forms.Form):

    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'name': 'email',
            'placeholder': 'E-mail',
            'class': 'form-control'
        })
    )
    username = forms.CharField(
        label="Nome de usuário",
        max_length=30,
        widget=forms.TextInput(attrs={
            'id': 'username',
            'name': 'username',
            'placeholder': 'Nome de usuário',
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
    confirm_password = forms.CharField(
        label="Confirme sua senha",
        widget=forms.PasswordInput(attrs={
            'id': 'confirm_password',
            'name': 'confirm_password',
            'placeholder': 'Confirme sua senha',
            'class': 'form-control'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', 'As senhas não conferem.')
        return cleaned_data
    
    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user