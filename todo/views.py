import logging

from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from .models import UserTodo, Todo
from user.models import UserAccount

class ItemView(View):

    def get(self, request, username):
        if request.META['HTTP_ACCEPT'] == 'application/json':
            user = UserAccount.objects.get(username=username)
            userTodos = UserTodo.objects.filter(user_id=user.id)
            todoIds = list(map(lambda userTodo: userTodo.todo_id, userTodos))

            todos = list(Todo.objects.filter(pk__in=todoIds).values())

            return JsonResponse({"code" : 1, "data" : {"items" : todos}})
        else:
            return render(request, 'todo/list.html')
