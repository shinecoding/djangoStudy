from typing import ContextManager
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = { 'projects' : projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    print('project', projectObj)
    return render(request, 'projects/single-project.html', {'project': projectObj})

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        print(request.POST, instance=project)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        #form = ProjectForm(request.POST)

    context = {'form': form }
    return render(request, "projects/project_form.html", context)



def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    #해당 pk에 맞는 Project를 가져옴
    form = ProjectForm(instance=project)
    #instance는 바꾸고 싶은 폼

    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        #form = ProjectForm(request.POST)

    context = {'form': form }
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context) 