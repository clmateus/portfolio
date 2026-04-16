from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    description = models.TextField()
    techstack = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.title}'