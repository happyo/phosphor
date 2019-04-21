import logging

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserAccount

logger = logging.getLogger(__name__)

@csrf_exempt
def login(request):
    if request.method == 'POST':
         username = request.POST['username']
        try:
            user = UserAccount.objects.get(username=username)
        except UserAccount.DoseNotExist:
            return JsonResponse({'code' : 0, 'data' : { 'errorMessage' : '用户名密码错误！'}})
        response = JsonResponse({ 'username': request.POST['username'] })
        response.set_cookie(username, username)
        return response
    else:
        return render(request, 'user/loginIndex.html')

