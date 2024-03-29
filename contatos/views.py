from django.shortcuts import render, get_object_or_404, Http404,redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def contatos(request):
    contatos = Contato.objects.order_by('id').filter(mostrar=True)
    paginator = Paginator(contatos, 5)
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)
    return render(request, 'contatos/todos_contatos.html', {'contatos': contatos})


def index(request):
    return render(request, 'contatos/index.html')


def mostrar_detalhes(request, pk):
    detalhe = get_object_or_404(Contato, id=pk)
    if not detalhe.mostrar:
        raise Http404()

    return render(request, 'contatos/detalhes.html', {'detalhe': detalhe})


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Este campo não pode ficar vazio.')
        return redirect('url_contatos')

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo))

    paginator = Paginator(contatos, 5)
    page_number = request.GET.get('page')
    contatos = paginator.get_page(page_number)
    return render(request, 'contatos/todos_contatos.html', {'contatos': contatos})
