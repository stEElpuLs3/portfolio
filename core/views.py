from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import Projeto
from django.http import FileResponse
import os


def miaudotefotos(request):
    return render(request, 'miaudotefotos.html')

def calendariofotos(request):
    return render(request, 'calendariofotos.html')

def home(request):
    return render(request, 'main.html')

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})

def contact (request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        # Envie o e-mail (opcional)
        send_mail(
            f'Contato: {assunto}',
            f'Nome: {nome}\nE-mail: {email}\nMensagem: {mensagem}',
            settings.EMAIL_HOST_USER,
            ['vitorvrp7@gmail.com'],  # Substitua pelo seu e-mail
            fail_silently=False,
        )

        # Redirecione para uma página de sucesso
        return redirect('contactsuccess')

    return render(request, 'contact.html')


def contactsuccess (request):
    return render(request, 'contactsuccess.html')


def curriculo(request):
    
    # Caminho absoluto para o arquivo PDF
    curriculo_path = os.path.join('static', 'curriculo.pdf')
    
    # Abrindo o arquivo PDF e retornando como resposta
    try:
        return FileResponse(open(curriculo_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        return render(request, 'core/erro.html')