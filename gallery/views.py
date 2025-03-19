from django.shortcuts import get_object_or_404, render

from gallery.models import Photograph



def index(request):
    photographs = Photograph.objects.all()
    return render(request, 'galerry/index.html', {"cards": photographs})


def imagem(request, photo_id):
    photograph = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'galerry/imagem.html', {"photograph": photograph})