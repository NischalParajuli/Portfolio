from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache
from .models import *
from django.http import FileResponse, Http404, JsonResponse
from django.conf import settings

@never_cache
def home(request):
    user = UserProfile.objects.first()
    skills = Skill.objects.all()
    user.summary="Results-driven Python Developer specializing in backend development, building scalable APIs and web systems with Django and Flask. Skilled in Python, SQL, and database management, with a focus on clean, efficient, and high-performance code."
    user.college_location = "Gauradaha, Jhapa"
    user.school_location = "Gauradaha, Jhapa"
    return render(request, 'home.html', {'user': user, 'skills': skills})

@never_cache
def projects(request):
    projects = Project.objects.all()
    user = UserProfile.objects.first()
    return render(request, 'projects.html', {'user': user, 'projects': projects})

@never_cache
def project_detail(request, pk):
    user = UserProfile.objects.first()
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_details.html', {'user': user, 'project': project})

def download_resume(request):
    try:
        resume = Resume.objects.latest('uploaded_at')
        return FileResponse(resume.file.open('rb'), as_attachment=True, filename=resume.file.name)
    except Resume.DoesNotExist:
        raise Http404("Resume not found")