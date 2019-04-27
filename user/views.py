import logging
import jwt

from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.conf import settings

from common.utils.ResponseHelper import normalJsonResponse, errorJsonResponse
from .models import UserAccount

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):

    def get(self, request):
        return render(request, 'user/loginIndex.html')

    def post(self, request):
        username = request.POST['username']
        try:
            user = UserAccount.objects.get(username=username)
        except UserAccount.DoesNotExist:
            return errorJsonResponse('Incorrect username or password')
        response = normalJsonResponse({ 'username': request.POST['username'] })
        token = jwt.encode({'username' : user.username}, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        # logging.error(token)
        response.set_cookie('token', token)
        return response

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(View):

    def get(self, request):
        return render(request, 'user/join.html')

    def post(self, request):
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
            return normalJsonResponse({})
        else:
            return errorJsonResponse('User already exists')

