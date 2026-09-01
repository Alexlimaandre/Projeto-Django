from django.shortcuts import render
from .models import Todo

def home(req):
    return render(req, "todos/home.html")

def todo_list(req):
    nome = "Alex"
    todos = Todo.objects.all()
    alunos = ["João", "Maria", "Pedro"]
    return render(req, "todos/todo_list.html", {'nome':nome, 'alunos':alunos, "todo": todos})


