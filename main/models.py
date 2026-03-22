from django.db import models

class UserProfile(models.Model):
  fullname = models.CharField(max_length=50)
  degree = models.CharField(max_length=250)
  course = models.CharField(max_length=250)
  linkdin = models.URLField()
  facebook = models.URLField()
  instagram = models.URLField()
  github = models.URLField()
  summary = models.TextField()
  image = models.ImageField(upload_to="media/profile/", height_field=None, width_field=None, max_length=None)

  # 12th
  college_name = models.CharField(max_length=250, blank=True)
  college_location = models.CharField(max_length=50, blank=True)

  # 10th
  school_name = models.CharField(max_length=250, blank=True)
  school_location = models.CharField(max_length=50, blank=True)

  def __str__(self):
      return self.fullname

class Skill(models.Model):
  name = models.CharField(max_length=100)
  skill_img = models.ImageField(upload_to="skills/", blank=True, null=True)

  def __str__(self):
    return self.name

class Project(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to="projects/", height_field=None, width_field=None, max_length=None)
  project_details = models.TextField(blank = False , null=True)
  github_repo = models.URLField()

class Resume(models.Model):
  name = models.CharField(max_length=100)
  file = models.FileField(upload_to='resumes/')
  uploaded_at = models.DateTimeField(auto_now_add=True)


  def __str__(self):
    return self.name