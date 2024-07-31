from django.urls import path

from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.task_lista, name='task_lista'),
    path('task/<int:id>/', views.task_detalhes, name='task_detalhes'),
    path('criar/', views.criar_task, name='criar_task'),
    path('editar/<int:id>/', views.editar_task, name='editar_task'),
    path('deletar/<int:id>/', views.deletar_task, name='deletar_task'),
    path(
        'alterarstatus/<int:id>/', views.alterar_status, name='alterar_status'
    ),
]