from django.shortcuts import render
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    contex = {'profiles': profiles}
    return render(request, 'users/profiles.html', contex)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')
    context = {'profile': profile, 'topSkills': top_skills, 'otherSkills': other_skills}
    return render(request, 'users/user_profile.html', context)