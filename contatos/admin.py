from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome',)
    list_editable = ('telefone', 'mostrar')
    list_per_page = 10
    search_fields = ('nome',)


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)