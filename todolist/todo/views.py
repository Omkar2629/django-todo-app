from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoList, Task

class HomeView(ListView):
    model = TodoList
    template_name = 'todo/home.html'
    context_object_name = 'lists'

class AddListView(CreateView):
    model = TodoList
    fields = ['name', 'due_datetime']
    template_name = 'todo/add_list.html'
    success_url = reverse_lazy('home')

class DeleteListView(DeleteView):
    model = TodoList
    template_name = 'todo/delete_list.html'
    success_url = reverse_lazy('home')

class AddTaskView(CreateView):
    model = Task
    fields = ['todolist', 'title', 'due_datetime']
    template_name = 'todo/add_task.html'
    success_url = reverse_lazy('home')

class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'todo/delete_task.html'
    success_url = reverse_lazy('home')