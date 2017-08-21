from django.db import models
from tinymce.models import HTMLField
from datetime import datetime
from tinymce import models as tinymce_models

class Project(models.Model):
    name = models.CharField(max_length=100)
    added = models.DateTimeField(default=datetime.now)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)


class Assessment(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    added = models.DateTimeField(default=datetime.now)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)


class Sh0t(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField(null=True)
    assessment = models.ForeignKey(Assessment, null=True, on_delete=models.SET_NULL)
    added = models.DateTimeField(default=datetime.now)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)


class Flag(models.Model):
    title = models.CharField(max_length=100)
    note = HTMLField(null=True)
    assessment = models.ForeignKey(Assessment, null=True, on_delete=models.SET_NULL)
    done = models.BooleanField(default=False)
    added = models.DateTimeField(default=datetime.now)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)


class Template(models.Model):
    name = models.CharField(max_length=100)
    body = tinymce_models.HTMLField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)

