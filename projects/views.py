from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    msg = 'Hello, projects page here'
    number = 1112
    context = {'msg': msg, 'number': number}
    return render(request, 'projects/projects.html', context)

def project(request):
    return render(request, 'projects/single-project.html')