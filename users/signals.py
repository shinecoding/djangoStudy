from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

#시그널 리시버
#아래 주석은 데코레이터가 정식명칭으로 시그널을 표현하는 또 다른 방법
#@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    print('Profile signal triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,

        )
    # print('Profile Saved!')
    # print('Instance:', instance)
    # print('Created', created)

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    #instance=Profile, sender=Profile
    print('Deleting user...')

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)