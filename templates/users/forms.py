from django import forms

class LoginForms(forms.Form):
    nomeLogin = forms.CharField(
        label='nome de login', required=True, max_length=100, widget=forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ex: João Silva'
            }
        )
    )
    password = forms.CharField(
        label='senha', required=True, max_length=70, widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class RegisterForms(forms.Form):
    name_register = forms.CharField(
        label='Nome de cadastro', required=True, max_length=100, widget=forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ex: João Silva'
            }
        )
    )

    email = forms.EmailField(
        label='Email', required=True, max_length=100, widget=forms.EmailInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Ex: joao.silva@gmail.com'
            }
        )
    )

    password1 = forms.CharField(
        label='Senha', required=True, max_length=70, widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    password2 = forms.CharField(
        label='Confirme sua senha', required=True, max_length=70, widget=forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )

    def clean_name_register(self):
        nome=self.cleaned_data.get('name_register')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não é possível cadastrar o usuário com espaços')
            else:
                return nome

