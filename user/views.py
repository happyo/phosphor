import logging
import jwt

from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.conf import settings

from common.utils.ResponseHelper import normalJsonResponse, errorJsonResponse
from .models import UserAccount

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
        token = jwt.encode({'username' : user.username}, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        logging.error(token)
        response.set_cookie('token', token)
        return response
    else:
        logger.error(request)
        logger.error(request.META['HTTP_ACCEPT'])
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
