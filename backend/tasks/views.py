from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from tasks.filters import TaskFilter
from tasks.models import Task
from tasks.serializers import TaskListSerializer, TaskDetailSerializer


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TaskFilter
    ordering = ['-created_at']


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer

    http_method_names = ['get', 'patch', 'delete']
