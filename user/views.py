import logging

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        logger.error(request.POST)
        return JsonResponse({ 'username': 'happyo' })
    else:
        return render(request, 'user/loginIndex.html')

