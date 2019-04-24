from django.http import JsonResponse

def errorJsonResponse(errorMessage):
    return JsonResponse({'code' : 0, 'data' : { 'errorMessage' : errorMessage }})

def normalJsonResponse(jsonData):
    return JsonResponse({'code' : 1, 'data' : jsonData});
