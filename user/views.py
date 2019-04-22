import logging

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import UserAccount
from django.urls import reverse

logger = logging.getLogger(__name__)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            user = UserAccount.objects.get(username=username)
        except UserAccount.DoesNotExist:
            return errorJsonResponse('Incorrect username or password')
        response = normalJsonResponse({ 'username': request.POST['username'] })
        response.set_cookie(user_id, user.id)
        return response
    else:
        logger.error(request)
        return render(request, 'user/loginIndex.html')

@csrf_exempt
def join(request):
    if request.method == 'GET':
        return render(request, 'user/join.html')
    elif request.method == 'POST':
        params = request.POST
        username = params['username']
        password = params['password']
        try:
            user = UserAccount.objects.get(username=username)
        except UserAccount.DoesNotExist:
            newUser = UserAccount()
            newUser.username = username
            newUser.password = password
            newUser.save()
            return HttpResponseRedirect(reverse('user:haha'))
        else:
            return errorJsonResponse('User already exists')

def haha(request):
    return render(request, 'user/haha.html')

def errorJsonResponse(errorMessage):
    return JsonResponse({'code' : 0, 'data' : { 'errorMessage' : errorMessage }})

def normalJsonResponse(jsonData):
    return JsonResponse({'code' : 1, 'data' : jsonData});
