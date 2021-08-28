from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our products')

def project(request, pk):
    return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))