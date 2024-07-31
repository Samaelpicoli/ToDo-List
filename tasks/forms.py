from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    """
    Formulário para criação e atualização de tarefas.

    Este formulário usa o modelo `Task` e inclui os campos 
    `titulo` e `descricao` para permitir a criação e edição 
    de tarefas.

    Meta:
        model (Task): O modelo associado a este formulário.
        fields (tuple): Os campos do modelo a serem 
        incluídos no formulário.
    """
    class Meta:
        model = Task
        fields = ('titulo', 'descricao')