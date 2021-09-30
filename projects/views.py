from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.db.models import Q
from .models import Project, Tag
from .forms import ProjectForm
from .utils import searchProjects



def projects(request):
    projects, search_query = searchProjects(request)

    page = request.GET.get('page')
    results = 3 #한페이지에 몇개씩 보여주는지
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger: #처음 들어왔을 때 파라미터가 없어서 나는 에러
        page = 1 
        projects = paginator.page(page) #1로 셋팅
    except EmptyPage: #페이지수 10000을 넣었을 때 뜨는 에러
        page = paginator.num_pages #페이지 총수
        projects = paginator.page(page)
        
    context = { 'projects' : projects, 'search_query': search_query, 'paginator':paginator}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    print('project', projectObj)
    return render(request, 'projects/single-project.html', {'project': projectObj})


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == 'POST':
        
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
        #form = ProjectForm(request.POST)

    context = {'form': form }
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    #해당 pk에 맞는 Project를 가져옴
    form = ProjectForm(instance=project)
    #instance는 바꾸고 싶은 폼

    if request.method == 'POST':
       #print(request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
        #form = ProjectForm(request.POST)

    context = {'form': form }
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context) 