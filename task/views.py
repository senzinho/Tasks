from django.shortcuts import render, redirect, get_object_or_404
from task.models import tasks
from task.forms import taskForm

def tarefa_view(request):
    tarefas = tasks.objects.all()
    

    return render(request, 'index.html',
                  {'tasks': tarefas}
                  
                  )


# nova tarefa
def new_task_view(request):
    if request.method == 'POST':
        new_task_form = taskForm(request.POST)
        if new_task_form.is_valid():
            new_task_form.save()
            return redirect('list_task')
    else:
        new_task_form = taskForm()
    return render(request, 'new_task.html', { 'new_task_form': new_task_form})


# excluir tarefa
def delete_task_view(request, pk):
    task = get_object_or_404(task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('list_task')
    return render(request, 'delete_task.html', {'task': task})

    
