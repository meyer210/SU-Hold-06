from django.shortcuts import render, get_object_or_404
from .models import Project
from django.views import generic
# Create your views here.
class indexView(generic.ListView):
    template_name = "Projects/index.html"
    context_object_name = 'latestProjectList'

    def get_queryset(self):
        Project.objects.order_by('-title')
    def creatProject(self,):

class detailView(generic.DetailView):
    model = Project
    template_name = "Projects/detail.html"



def index(request):
    latestProjectList = Project.objects.order_by('-title')
    output = {'latestProjectList':  latestProjectList}
    return render(request, 'Projects/index.html', output)

def detail(request, project_id):
    output = get_object_or_404(Project, pk=project_id)
    return render(request, 'Projects/detail.html', {'Project' : output})
