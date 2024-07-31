from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class InscreverSe(generic.CreateView):
    """
    View para o formulário de inscrição de usuários.

    Esta view herda de `generic.CreateView` e utiliza o formulário 
    padrão de criação de usuários (`UserCreationForm`).

    Após a criação bem-sucedida do usuário, redireciona para a 
    página de login.

    Attributes:
        form_class (UserCreationForm): O formulário usado para 
        criar novos usuários.
        success_url (str): URL para redirecionamento após a criação 
        bem-sucedida do usuário.
        template_name (str): Caminho do template a ser renderizado
        para a inscrição do usuário.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registrar.html'
