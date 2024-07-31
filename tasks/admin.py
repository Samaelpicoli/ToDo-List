from django.contrib import admin

from tasks.models import Task

"""
Registro do modelo Task no admin do Django.

Este módulo registra o modelo `Task` no site de administração do Django
para que as tarefas possam ser gerenciadas através da interface 
administrativa.
"""
admin.site.register(Task)