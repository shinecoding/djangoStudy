from django.shortcuts import render
from .models import Profile
from selenium import webdriver
from time import sleep

def profiles(request):
    # r = requests.get('https://xkcd.com/353/')
    # print(r.text)
    url = input("Which page would you like to check? Enter Full URL: ")
    keyword = input("What is your seo keyword? ")

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.theverge.com/')
        sleep(2)
        fb_btn = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/header/div/div[2]/div[1]/ul/li[2]/a')
        fb_btn.click()

    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile':profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)
    