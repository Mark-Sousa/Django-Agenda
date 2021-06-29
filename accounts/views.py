from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import FormContato
from contatos.models import Contato


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'usuário ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        return redirect('url_contatos')


def logout(request):
    auth.logout(request)
    return redirect('url_index')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.add_message(request, messages.ERROR, 'nenhum campo pode ficar vazio.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.ERROR, 'Email Inválido')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.add_message(request, messages.ERROR, 'Usuário precisa de 6 caracteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.add_message(request, messages.ERROR, 'Senha precisa de 6 caracteres ou mais')
        return render(request, 'accounts/cadastro.html')

    if senha2 != senha:
        messages.add_message(request, messages.ERROR, 'Senhas não conferem')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.ERROR, 'Usuário ja cadastrado')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.ERROR, 'Email ja cadastrado')
        return render(request, 'accounts/cadastro.html')

    messages.add_message(request, messages.SUCCESS, 'registrado com sucesso, Agora faça login! ')
    user = User.objects.create_user(username=usuario, first_name=nome, last_name=sobrenome, email=email, password=senha)
    user.save()
    return redirect('url_login')


def editar_cadastro(request, pk):
    contato_antigo = Contato.objects.get(id=pk)
    form = FormContato(request.POST or None, instance=contato_antigo)
    if form.is_valid():
        form.save()
        return redirect('url_contatos')
    return render(request, 'accounts/dashboard.html', {'form': form})


def deletar_contato(request, pk):
    contato = Contato.objects.get(id=pk)
    contato.delete()
    return redirect('url_contatos')


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = FormContato(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']
            data_criacao = form.cleaned_data['data_criacao']
            descricao = form.cleaned_data['descricao']
            categoria = form.cleaned_data['categoria']
            mostrar = form.cleaned_data['mostrar']
            imagem = form.cleaned_data['imagem']

            Contato.objects.create(nome=nome, sobrenome=sobrenome, telefone=telefone, email=email,
                                   data_criacao=data_criacao, descricao=descricao, categoria=categoria, mostrar=mostrar,
                                   imagem=imagem)
            return redirect('url_contatos')

    else:
        form = FormContato()

    return render(request, 'accounts/dashboard.html', {'form': form})