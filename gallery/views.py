from django.shortcuts import render


def index(request):
    return render(request, 'galerry/index.html')

def imagem(request):
    return render(request, 'galerry/imagem.html')