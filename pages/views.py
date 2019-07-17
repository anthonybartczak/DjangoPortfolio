from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.

def index(request):
	return render(request, 'index.html')