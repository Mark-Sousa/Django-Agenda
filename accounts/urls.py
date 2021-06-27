from django.urls import path
from .views import login, logout, cadastro,  dashboard, editar_cadastro


urlpatterns = [
    path('', login, name="index_login"),
    path('login/', login, name="url_login"),
    path('logout/', logout, name="url_logout"),
    path('cadastro/', cadastro, name="url_cadastro"),
    path('dashboard/', dashboard, name="url_dashboard"),
    path('editar_cadastro/<int:pk>/', editar_cadastro, name="url_editar_cadastro"),
]