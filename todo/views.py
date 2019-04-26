import logging

from django.shortcuts import render
from django.views.generic.base import View
from django.core import serializers
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict

from .models import UserTodo, Todo
from user.models import UserAccount
from common.utils.ResponseHelper import normalJsonResponse, errorJsonResponse
from user.auth.permission import auth_permission_required

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(auth_permission_required, name='dispatch')
class TodoListView(View):

    def get(self, request, username):
        if request.META['HTTP_ACCEPT'] == 'application/json':
            user = UserAccount.objects.get(username=username)
            userTodos = UserTodo.objects.filter(user_id=user.id)
            todoIds = list(map(lambda userTodo: userTodo.todo_id, userTodos))

            todos = list(Todo.objects.filter(pk__in=todoIds).values())

            return normalJsonResponse({"items" : todos})
        else:
            return render(request, 'todo/list.html')

    def post(self, request, username):
        if request.META['HTTP_ACCEPT'] == 'application/json':
            logging.error('get')
            try:
                title = request.POST['title']
                detail = request.POST['detail']

                todo = Todo()
                todo.title = title;
                todo.detail = detail;
                todo.save()

                user = UserAccount.objects.get(username=username)

                userTodo = UserTodo()
                userTodo.user_id = user.id
                userTodo.todo_id = todo.id
                userTodo.save()

                return normalJsonResponse({})
            except KeyError:
                return errorJsonResponse('error ')
            else:
                return normalJsonResponse({})
        else:
            return render(request, 'todo/add.html')

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(auth_permission_required, name='dispatch')
class TodoView(View):

    def get(self, request, username, todo_id):
        if request.META['HTTP_ACCEPT'] == 'application/json':
            todo = Todo.objects.get(pk=todo_id)
            return normalJsonResponse({"item" : { "title" : todo.title, "id" : todo.id, "detail" : todo.detail}})
        else:
            return render(request, 'todo/edit.html')

    def put(self, request, username, todo_id):
        put_params = QueryDict(request.body)
        todo = Todo.objects.get(pk=todo_id)
        if 'title' in put_params:
            title = put_params['title']
            todo.title = title
        if 'detail' in put_params:
            detail = put_params['detail']
            todo.detail = detail
        if 'status' in put_params:
            status = put_params['status']
            todo.status = status
        todo.save()
        return normalJsonResponse({})

    def delete(self, request, username, todo_id):
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
        return normalJsonResponse({})

@auth_permission_required
def createItemPage(request, username):
    return render(request, 'todo/add.html')
