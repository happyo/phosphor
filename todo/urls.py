from django.urls import path

from .views import TodoListView, TodoView, createItemPage

app_name = 'todo'
urlpatterns = [
    path('<str:username>/todos', TodoListView.as_view(), name='items'),
    path('<str:username>/todos/new', createItemPage, name='create_item_page'),
    path('<str:username>/todos/<int:todo_id>/', TodoView.as_view(), name='item'),
]
