from django.urls import path

from .views import TodoListView, TodoView

app_name = 'todo'
urlpatterns = [
    path('<str:username>/todos/', TodoListView.as_view(), name='items'),
    path('<str:username>/todos/<int:todo_id>/', TodoView.as_view, name='item'),
]
