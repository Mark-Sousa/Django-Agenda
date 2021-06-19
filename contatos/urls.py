from django.urls import path
from .views import index, mostrar_detalhes, busca

urlpatterns = [
    path('', index, name='url_index'),
    path('busca/', busca, name='url_busca'),
    path('mostrar_detalhes/<int:pk>/', mostrar_detalhes, name='url_mostrar'),
]