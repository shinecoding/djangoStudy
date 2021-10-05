from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProjects(request, projects, results):
    page = request.GET.get('page')
    #results = 3 #한페이지에 몇개씩 보여주는지
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger: #처음 들어왔을 때 파라미터가 없어서 나는 에러
        page = 1 
        projects = paginator.page(page) #1로 셋팅
    except EmptyPage: #페이지수 10000을 넣었을 때 뜨는 에러
        page = paginator.num_pages #페이지 총수
        projects = paginator.page(page)
        
    leftIndex = (int(page) - 4)
    if leftIndex <1 :
        leftIndex = 1

    rightIndex = (int(page) + 5) 
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages +1

    custom_range = range(leftIndex, rightIndex) #페이지바 갯수 설정가능
    return custom_range, projects


def searchProjects(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    #many to many 관계에 있는 태그
    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        #부모 owner 접근해서 name가져와서 필터링
        Q(tags__in=tags)
        #(좌)프로젝트의 tags가 (우)검색어 tags 에 포함되는지
    )

    return projects, search_query