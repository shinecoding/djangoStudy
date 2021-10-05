from django.db.models import Q
from .models import Profile, Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    #results = 3 #한페이지에 몇개씩 보여주는지
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger: #처음 들어왔을 때 파라미터가 없어서 나는 에러
        page = 1 
        profiles = paginator.page(page) #1로 셋팅
    except EmptyPage: #페이지수 10000을 넣었을 때 뜨는 에러
        page = paginator.num_pages #페이지 총수
        profiles = paginator.page(page)
        
    leftIndex = (int(page) - 4)
    if leftIndex <1 :
        leftIndex = 1

    rightIndex = (int(page) + 5) 
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages +1

    custom_range = range(leftIndex, rightIndex) #페이지바 갯수 설정가능
    return custom_range, profiles




def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        #print('SEARCH:', search_query)

    skills = Skill.objects.filter(name__icontains=search_query)

    #icontains 대소문자 구분없이 필터
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills))

    return profiles, search_query