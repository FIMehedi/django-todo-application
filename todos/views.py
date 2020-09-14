from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse

from .models import Todo


def list_todo_item(request):
    context = {'task_list': Todo.objects.all()}
    return render(request, 'todos/task_list.html', context)

def insert_todo_item(request:HttpRequest):
    task = request.POST['task']
    todo = Todo(task=task)
    todo.save()
    return redirect(reverse('todo_list'))

def remove_todo_item(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect(reverse('todo_list'))


