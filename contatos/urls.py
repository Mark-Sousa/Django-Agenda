from django.urls import path
from .views import index, mostrar_detalhes, busca, contatos

urlpatterns = [
    path('', index, name='url_index'),
    path('contatos/', contatos, name='url_contatos'),
    path('busca/', busca, name='url_busca'),
    path('mostrar_detalhes/<int:pk>/', mostrar_detalhes, name='url_mostrar'),
]