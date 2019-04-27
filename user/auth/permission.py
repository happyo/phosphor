import logging
import jwt

from django.conf import settings
from django.http import JsonResponse

from common.utils.ResponseHelper import errorJsonResponse

def auth_permission_required(view_func):

    def warpper(request, *args, **kwargs):
        # token = request.META['token']
        try:
            token = request.COOKIES['token']
            logging.error('request:'+ token)
            dict = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            username = dict['username']
            logging.error(username)
            path = request.path
            logging.error(path)
            if path.startswith('/' + username):
                return view_func(request, *args, **kwargs)
        except KeyError:
            return errorJsonResponse('Please login in the web site!')
        else:
            return errorJsonResponse('PermissionDenied!')

    return warpper
