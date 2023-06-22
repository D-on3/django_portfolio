from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.TextField()
    education = models.TextField()
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name