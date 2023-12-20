from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.forms import TaskForm

# Create your views here.
@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
    }
    return render(request, "projects/details.html", context)


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.author = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    
    context = {
        "form": form,
    }
    return render(request, 'tasks/create.html', context)
