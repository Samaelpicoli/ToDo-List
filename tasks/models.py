from django.contrib.auth import get_user_model
from django.db import models


STATUS = (
    ('fazendo', 'Fazendo'),
    ('finalizado', 'Finalizado'),
)

# Create your models here.
class Task(models.Model):
    """
    Modelo para representar uma tarefa.

    Attributes:
        user (ForeignKey): Referência ao usuário que criou a tarefa.
        titulo (CharField): O título da tarefa.
        descricao (TextField): A descrição detalhada da tarefa.
        status (CharField): O status atual da tarefa, pode ser 'fazendo'
        ou 'finalizado'.
        criado_em (DateTimeField): Data e hora de criação da tarefa.
        atualizado_em (DateTimeField): Data e hora da última atualização 
        da tarefa.
    """
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """
        Retorna a representação em string da tarefa.

        Returns:
            str: O título da tarefa.
        """
        return f'{self.titulo}'
    