from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from tasks.forms import TaskForm
from tasks.models import Task

# Create your views here.
@login_required
def task_lista(request):
    """
    Exibe a lista de tarefas do usuário.

    Essa view exibe a lista de tarefas do usuário logado, permite 
    buscar por título ou filtrar por status, e faz a paginação 
    dos resultados.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.

    Returns:
        HttpResponse: A resposta HTTP com o template 'lista.html' 
        renderizado e o contexto das tarefas.
    """
    task_lista = Task.objects.all().order_by('-criado_em')
    template_name = 'lista.html'

    tasks_feitas_recentemente = Task.objects.filter(
        status = 'finalizado', 
        atualizado_em__gt = datetime.now()-timedelta(days=30),
        user = request.user
    ).count()

    tasks_finalizadas = Task.objects.filter(
        status = 'finalizado', 
        user = request.user
    ).count()

    tasks_fazendo = Task.objects.filter(
        status = 'fazendo', 
        user = request.user
    ).count()

    search = request.GET.get('search')
    _filter = request.GET.get('filter')

    if search:
        tasks = Task.objects.filter(
            titulo__icontains=search, user=request.user
        )

    elif _filter:
        tasks = Task.objects.filter(status=_filter, user=request.user)

    else:
        paginator = Paginator(task_lista, 2)

        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, template_name, context={
        'tasks': tasks,
        'tasks_feitas_recentemente': tasks_feitas_recentemente,
        'tasks_finalizadas': tasks_finalizadas,
        'tasks_fazendo': tasks_fazendo
    })

@login_required
def task_detalhes(request, id):
    """
    Exibe os detalhes de uma tarefa específica.

    Essa view exibe os detalhes de uma tarefa específica baseada no
    ID fornecido.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.
        id (int): O ID da tarefa a ser exibida.

    Returns:
        HttpResponse: A resposta HTTP com o template 
        'task_detalhes.html' renderizado e o contexto da tarefa.
    """
    task = get_object_or_404(Task, pk=id)
    template_name = 'task_detalhes.html'
    return render(request, template_name, context={'task': task})

@login_required
def criar_task(request):
    """
    Cria uma nova tarefa.

    Essa view permite ao usuário criar uma nova tarefa. 
    Se o método da solicitação for POST, 
    os dados do formulário são validados e a tarefa é salva. 
    Caso contrário, exibe o formulário vazio.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.

    Returns:
        HttpResponse: A resposta HTTP com o template 'nova_task.html' 
        renderizado e o formulário de criação.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.status = 'fazendo'
            task.save()
            return redirect('/tasks')
    template_name = 'nova_task.html'
    form = TaskForm()
    return render(request, template_name, context={'form': form})


@login_required
def editar_task(request, id):
    """
    Edita uma tarefa existente.

    Essa view permite ao usuário editar uma tarefa existente. 
    Se o método da solicitação for POST, os dados do formulário são 
    validados e a tarefa é atualizada. Caso contrário, exibe o 
    formulário preenchido com os dados da tarefa.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.
        id (int): O ID da tarefa a ser editada.

    Returns:
        HttpResponse: A resposta HTTP com o template 'editar_task.html'
        renderizado e o formulário de edição.
    """
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'fazendo'
            task.save()
            return redirect('/tasks')
        else:
            return render(
                request, template_name, context={'form': form, 'task': task}
            )
    else:
        template_name = 'editar_task.html'
        return render(
            request, template_name, context={'form': form, 'task': task}
        )
    
@login_required
def deletar_task(request, id):
    """
    Deleta uma tarefa existente.

    Essa view permite ao usuário deletar uma tarefa 
    existente com base no ID fornecido.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.
        id (int): O ID da tarefa a ser deletada.

    Returns:
        HttpResponse: Redireciona para a lista de tarefas 
        após deletar a tarefa.
    """
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/tasks')


@login_required
def alterar_status(request, id):
    """
    Altera o status de uma tarefa existente.

    Essa view permite ao usuário alterar o status de uma tarefa
    entre 'fazendo' e 'finalizado'.

    Args:
        request (HttpRequest): O objeto de solicitação HTTP.
        id (int): O ID da tarefa a ter o status alterado.

    Returns:
        HttpResponse: Redireciona para a lista de tarefas após 
        alterar o status da tarefa.
    """
    task = get_object_or_404(Task, pk=id)
    if task.status == 'fazendo':
        task.status = 'finalizado'
    else:
        task.status = 'fazendo'

    task.save()
    return redirect('/tasks')
