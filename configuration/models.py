# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from tinymce import models as tinymce_models


class ModuleMaster(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)


class CaseMaster(models.Model):
    name = models.CharField(max_length=100)
    module = models.ForeignKey(ModuleMaster, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)


class TemplateMaster(models.Model):
    name = models.CharField(max_length=100)
    body = tinymce_models.HTMLField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
