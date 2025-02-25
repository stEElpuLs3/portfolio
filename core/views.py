from django.shortcuts import render
from .models import Projeto
from django.http import FileResponse
import os

def projetos(request):
    projetos_list = Projeto.objects.all()
    return render(request, 'core/projetos.html', {'projetos': projetos_list})



def curriculo(request):
    # Caminho absoluto para o arquivo PDF
    curriculo_path = os.path.join('static', 'curriculo.pdf')
    
    # Abrindo o arquivo PDF e retornando como resposta
    try:
        return FileResponse(open(curriculo_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        return render(request, 'core/erro.html')