from django.db import models

class tasks(models.Model):
    id = models.AutoField(primary_key=True)#auto incremento
    task_name = models.CharField(max_length=100)
    task_description = models.CharField(max_length=50,blank=True)
    task_date = models.DateField(blank=True) #data da execução da tarefa
    
    

    def __str__(self):
        return self.task_name

        