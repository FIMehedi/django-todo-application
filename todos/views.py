from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Todo


# def list_todo_item(request):
#     context = {'task_list': Todo.objects.all()}
#     return render(request, 'task_list.html', context)

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'task_list.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user)



# def insert_todo_item(request:HttpRequest):
#     task = request.POST['task'].strip()
#     if task != '':
#         todo = Todo(task=task)
#         todo.save()
#     return redirect(reverse('todo_list'))


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'task_list.html'
    fields = ['task']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# def remove_todo_item(request, id):
#     task = Todo.objects.get(id=id)
#     task.delete()
#     return redirect(reverse('todo_list'))

class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    template_name = 'task_list.html'
    success_url = reverse_lazy('todo_list')

    def test_func(self):
        return self.get_object().user == self.request.user
