from django.shortcuts import render


# Create your views here.
def index(request):
    """
    View para a página inicial.

    Renderiza o template 'index.html' para a página inicial do site.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.

    Returns:
        HttpResponse: A resposta HTTP com o conteúdo renderizado 
        do template 'index.html'.
    """
    return render(request, 'index.html')