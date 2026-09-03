from django.views.generic import ListView, CreateView
from .models import Todo
from django.urls import reverse_lazy

# def todo_list(req):
#     nome = "Alex"
#     todos = Todo.objects.all()
#     alunos = ["João", "Maria", "Pedro"]
#     return render(req, "todos/todo_list.html", {'nome':nome, 'alunos':alunos, "todo": todos})

# Função acima é uma tradução da classe abaixo, que é uma forma mais simples de fazer a mesma coisa, mas com menos flexibilidade

class TodoHomeView(ListView):
    model = Todo
    template_name = "todos/home.html"
class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todo"

class TodoCreateView(CreateView):
    model = Todo
    template_name = "todos/todo_create.html"
    fields = ["title","deadline"] # Usando o CreateView, é necessário informar os fields que serão exibidos no formulário, ou seja, os campos que o usuário poderá preencher. Caso não seja informado, o Django exibirá todos os campos do modelo.
    success_url = reverse_lazy("todo_list") # Após o usuário preencher o formulário, ele será redirecionado para a página de listagem de tarefas. O reverse_lazy é usado para gerar a URL da view "todo_list" de forma dinâmica, sem precisar hardcodar a URL.
