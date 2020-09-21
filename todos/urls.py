from django.urls import path

from .views import (
    TodoListView,
    TodoCreateView,
    TodoDeleteView,
    )


urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('insert/', TodoCreateView.as_view(), name='todo_insert'),
    path('remove/<int:pk>/', TodoDeleteView.as_view(), name='todo_remove'),
]
