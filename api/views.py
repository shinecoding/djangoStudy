from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project
#django-rest-framework.org
#pip install djangorestframework

@api_view(['GET'])
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
    #return JsonResponse(routes, safe=False)
    #데코레이터 api_view 붙이고 리턴을 Response로 바꿈

    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

