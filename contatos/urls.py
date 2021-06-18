from django.urls import path
from .views import index, mostrar_detalhes

urlpatterns = [
    path('', index, name='url_index'),
    path('mostrar_detalhes/<int:pk>/', mostrar_detalhes, name='url_mostrar'),
]