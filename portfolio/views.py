from django.shortcuts import render
from.models import project

def index(request):
    projects = project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, title):
    projects = project.objects.get(title=title)
    context = {
        'projects': projects
    }
    return render(request, 'project_detail.html', context)

# Create your views here.
