from django.urls import path
from . import views
from .views import download_resume

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
     path('resume/', download_resume, name='download_resume'),
]