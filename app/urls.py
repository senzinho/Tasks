
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from task.views import tarefa_view,new_task_view, delete_task_view #importei a tasks_view da pasta task / views.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', tarefa_view, name='list_task'),
    path('new_task/', new_task_view, name='new_task'),
    path('delete_task/<int:pk>',delete_task_view, name='delete_task'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)