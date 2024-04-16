from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages


# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR,
                                 "A senha e confirmar senha devem ser iguais")
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR,
                                 "A senha deve ter no mínimo 6 dígitos")
            return redirect('/usuarios/cadastro')

        users = User.objects.filter(username=username)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha,
        )

        if users.exists():
            messages.add_message(request, constants.ERROR,
                                 "Já existe um usuário com esse username")
            return redirect('/usuarios/cadastro')

        return redirect('/usuarios/login')


def login(request):
    pass
