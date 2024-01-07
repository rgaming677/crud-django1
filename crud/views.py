from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages

from .models import Task
from .forms import TaskForm
# Create your views here.
def index_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }

    return render(request, 'crud/index.html', context)

def detail_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        context = {
            'task': task
        }
    except Task.DoesNotExist:
        raise Http404("Data tidak ditemukan.")
    
    return render(request, 'crud/detail.html', context)

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = TaskForm(request.POST)
            new_task.save()
            messages.success(request, 'Sukses menambah data baru.')
            return redirect('crud:index')
    else:
        form = TaskForm()
    return render(request, 'crud/form.html', {'form': form})

def update_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("data tidak ditemukan.")

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            messages.success(request, 'Sukses Mengubah Data.')
            return redirect('crud:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'crud/form.html', {'form': form})

def delete_view(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        messages.success(request, 'Sukses Menghapus Data.')
        return redirect('crud:index')
    except Task.DoesNotExist:
        raise Http404("Data tidak ditemukan.")