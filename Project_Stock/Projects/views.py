from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project

# Create your views here.
def index(request):
    latestProjectList = Project.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.title for p in latestProjectList])
    return render(request, 'Projects/index.html', {'latestProjectList' : output})

def detail(request, project_id):
    output = get_object_or_404(Project, pk=project_id)
    return render(request, 'Projects/detail.html', {'Project' : output})
