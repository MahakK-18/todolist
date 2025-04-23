from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def todolist(request):
    tasks = Task.objects.all().order_by('created_at')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    else:
        form = TaskForm()
    return render(request, 'todolist.html', {'tasks': tasks, 'form': form})

def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todolist')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todolist_update.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('todolist')
    return render(request, 'todolist.html', {'task': task})