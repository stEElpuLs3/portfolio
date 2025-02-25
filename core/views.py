from django.shortcuts import render
from django.core.mail import send_mail
from .models import Projeto
from django.http import FileResponse
import os


def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/projetos.html', {'projetos': projetos})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
            f'Contato de {name}',
            message,
            email,
            ['vitorvrp7@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'core/contact.html', {'success': True})
    return render(request, 'core/contact.html')


def curriculo(request):
    # Caminho absoluto para o arquivo PDF
    curriculo_path = os.path.join('static', 'curriculo.pdf')
    
    # Abrindo o arquivo PDF e retornando como resposta
    try:
        return FileResponse(open(curriculo_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        return render(request, 'core/erro.html')