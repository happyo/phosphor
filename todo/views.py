from django.shortcuts import render
from django.views.generic.base import View

class ItemView(View):

    def get(self, request, user_id):{
        return render(request, 'todo/list.html')
    }
