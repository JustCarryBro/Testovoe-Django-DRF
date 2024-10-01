from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializers
from django.shortcuts import render

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# ТУТ АПИ
class TaskApi(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

