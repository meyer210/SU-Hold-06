from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello")
def detail(request, Project_id):
    return HttpResponse("Porject #%s" % Project_id)