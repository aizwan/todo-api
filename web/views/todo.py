from rest_framework import viewsets
from rest_framework import filters

from web.models.todo import Todo
from web.serializers.todo import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        'id',
        'title',
        'description',
    )
    ordering_fields = (
        'title',
        'created_at',
        'updated_at'
    )