from django import forms
from task.models import tasks

class taskForm(forms.Form):
    task_name = forms.CharField(max_length=100)
    task_description = forms.CharField(max_length=50, required=False)
    task_date = forms.DateField(required=False)  # data da execução da tarefa


    def save(self):
        tarefas = tasks(
            task_name = self.cleaned_data['task_name'],
            task_description = self.cleaned_data['task_description'],
            task_date = self.cleaned_data['task_date'],

        )
        tarefas.save()
        return tarefas