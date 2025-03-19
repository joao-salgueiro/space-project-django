from django.urls import path
from gallery.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:photo_id>', imagem, name='imagem')
]
