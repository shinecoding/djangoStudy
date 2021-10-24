from django.http import JsonResponse

#django-rest-framework.org
#pip install djangorestframework

def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},
        

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
        
    ]

    #by default JsonResponse returns dictionary
    #Here, we are sending a list not a dictionary
    #safe param: can return something more than a python dictionary
    #False: turn any kind of data into Json data
    return JsonResponse(routes, safe=False)