from django.urls import path
from .views import login, logout, cadastro,  dashboard
urlpatterns = [
    path('', login, name="index_login"),
    path('login/', login, name="url_login"),
    path('logout/', logout, name="url_logout"),
    path('cadastro/', cadastro, name="url_cadastro"),
    path('dashboard/', dashboard, name="url_dashboard"),
]