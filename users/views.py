from django.shortcuts import redirect, render
from templates.users.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            name = form['nomeLogin'].value()
            password = form['password'].value()

            user = auth.authenticate(
                request,
                username=name,
                password=password
            )

            if user is not None:
                auth.login(request, user)
                messages.success(request, f'Usuário {name} logado')
                return redirect('index')
            else:
                messages.error(request, 'Falha ao efetuar login')
                return redirect('login')


    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 != password2:
                messages.error(request, 'Senhas não são iguais')
                form.add_error('password2', 'As senhas não coincidem.')
            elif User.objects.filter(username=form.cleaned_data['name_register']).exists():
                messages.error(request, 'Usuário já existente')
                form.add_error('name_register', 'Nome de usuário já existe.')
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['name_register'],
                    email=form.cleaned_data['email'],
                    password=password1
                )
                user.save()
                messages.success(request, 'Cadastro efetuado com sucesso')
                return redirect('login')  # Certifique-se de que 'login' é o nome correto da URL

    return render(request, 'users/register.html', {'form': form})


def logout(request):
    messages.success(request, 'Logout Efetuado com sucesso')
    auth.logout(request)
    return redirect('login')
