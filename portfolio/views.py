from django.shortcuts import render
from .data import hard_skills, projects

def home(request):
    return render(request, 'home.html', {'hard_skills': hard_skills})

def projects_view(request):
    return render(request, 'projects.html', {'projects': projects})

def details(request, id):
    project = projects.get(id)
    return render(request, 'details.html', {'project': project})