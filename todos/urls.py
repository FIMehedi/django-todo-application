from django.urls import path

from .views import list_todo_item, insert_todo_item, remove_todo_item


urlpatterns = [
    path('', list_todo_item, name='todo_list'),
    path('insert/', insert_todo_item, name='todo_insert'),
    path('remove/<int:id>/', remove_todo_item, name='todo_remove'),
]
