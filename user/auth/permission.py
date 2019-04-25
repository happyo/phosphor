import logging

from django.http import JsonResponse

def auth_permission_required(view_func):

    def warpper(request, *args, **kwargs):
        logging.error(request)
        return view_func(request, *args, **kwargs)

    return warpper
