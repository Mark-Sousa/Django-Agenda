from django.shortcuts import render, get_object_or_404, Http404
from .models import Contato
from django.core.paginator import Paginator


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
