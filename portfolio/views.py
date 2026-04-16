from django.shortcuts import render
# from .data import hard_skills, projects
from .models import Skill, Project

def home(request):
    skills = Skill.objects.all()
    return render(request, 'home.html', {'skills': skills})

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def details(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'details.html', {'project': project})