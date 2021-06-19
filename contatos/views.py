from django.shortcuts import render, get_object_or_404, Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    contatos = Contato.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(contatos, 5)
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)
    return render(request, 'contatos/index.html', {'contatos': contatos})


def mostrar_detalhes(request, pk):
    detalhe = get_object_or_404(Contato, id=pk)
    if not detalhe.mostrar:
        raise Http404()

    return render(request, 'contatos/detalhes.html', {'detalhe': detalhe})


def busca(request):
    termo = request.GET.get('termo')
    if termo is None:
        raise Http404

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo))
    print(contatos.query)
    paginator = Paginator(contatos, 5)
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)
    return render(request, 'contatos/index.html', {'contatos': contatos})
