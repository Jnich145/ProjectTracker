from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.views import list_projects


# Create your views here.
@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
    }
    return render(request, "projects/details.html", context)
