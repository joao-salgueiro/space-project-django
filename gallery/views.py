from django.shortcuts import get_object_or_404, render

from gallery.models import Photograph



def index(request):
    photographs = Photograph.objects.order_by("photo_date").filter(publicated=True)
    return render(request, 'galerry/index.html', {"cards": photographs})


def imagem(request, photo_id):
    photograph = get_object_or_404(Photograph, pk=photo_id)
    return render(request, 'galerry/imagem.html', {"photograph": photograph})

def search(request):
    photographs = Photograph.objects.order_by("photo_date").filter(publicated=True)

    if("search" in request.GET):
        search_name = request.GET['search']
        if search_name:
            photographs = photographs.filter(name__icontains=search_name)
    return render(request, 'galerry/search.html', {"cards": photographs})