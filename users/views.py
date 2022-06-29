from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


from .models import Profile


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            print("Username does not exists")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username or password is incorrect')


    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


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