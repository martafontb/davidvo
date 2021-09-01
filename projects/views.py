from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from next_prev import next_in_order, prev_in_order


# Create your views here.
def home(request):
    projects = Project.objects
    projects = projects.filter(is_visible=True)
    projects = projects.order_by("-rank", "title")
    
    return render(request, "home.html", {
        "projects": projects
    })

def project(request, slug):
    project = Project.objects.get(slug=slug)

    qs = Project.objects.filter(is_visible=True)
    next_project = next_in_order(project, loop=True, qs=qs)
    prev_project = prev_in_order(project, loop=True, qs=qs)

    return render(request, "project.html", {
        "project" : project,
        "prev_project" : prev_project,
        "next_project" : next_project
    })