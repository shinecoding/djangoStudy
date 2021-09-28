from .models import Project, Tag
from django.db.models import Q


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