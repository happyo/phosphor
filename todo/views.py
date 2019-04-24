import logging

from django.shortcuts import render
from django.views.generic.base import View
from django.core import serializers
from django.forms.models import model_to_dict

from .models import UserTodo, Todo
from user.models import UserAccount
from common.utils import ResponseHelper

class TodoListView(View):

    def get(self, request, username):
        if request.META['HTTP_ACCEPT'] == 'application/json':
            user = UserAccount.objects.get(username=username)
            userTodos = UserTodo.objects.filter(user_id=user.id)
            todoIds = list(map(lambda userTodo: userTodo.todo_id, userTodos))

            todos = list(Todo.objects.filter(pk__in=todoIds).values())

            return JsonResponse({"code" : 1, "data" : {"items" : todos}})
        else:
            return render(request, 'todo/list.html')

    def post(self, request):
        if request.META['HTTP_ACCEPT'] == 'application/json':
            try:
                title = request.POST['title']
                detail = request.POST['detail']
            except KeyError:
                return errorJsonResponse('error ')
            else:
                return normalJsonResponse({})
        else:
            return render(request, 'todo/add.html')

class TodoView(View):

    def get(self, request, username, todo_id):
        if request.META['HTTP_ACCEPT'] == 'application/json':
            todo = Todo.objects.get(pk=todo_id).values()
            return JsonResponse({"code" : 1, "data" : {"item" : todo}})
        else:
            return render(request, 'todo/edit.html')
