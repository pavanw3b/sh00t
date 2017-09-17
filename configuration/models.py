# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class MethodologyMaster(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    order = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="methodology_created_by", null=True)
    created = models.DateTimeField(default=datetime.now)
    updated_by = models.ForeignKey(User, related_name="methodology_updated_by", null=True)
    updated = models.DateTimeField(default=datetime.now)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(MethodologyMaster, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)


@python_2_unicode_compatible
class ModuleMaster(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    order = models.IntegerField(default=0)
    methodology = models.ForeignKey(MethodologyMaster, on_delete=models.CASCADE, null=True, default=None)
    created_by = models.ForeignKey(User, related_name="module_created_by", null=True)
    created = models.DateTimeField(default=datetime.now)
    updated_by = models.ForeignKey(User, related_name="module_updated_by", null=True)
    updated = models.DateTimeField(default=datetime.now)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(ModuleMaster, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)


@python_2_unicode_compatible
class CaseMaster(models.Model):
    name = models.CharField(max_length=100)
    module = models.ForeignKey(ModuleMaster, on_delete=models.CASCADE)
    description = models.TextField(default="")
    order = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, related_name="case_module_created_by", null=True)
    created = models.DateTimeField(default=datetime.now)
    updated_by = models.ForeignKey(User, related_name="case_module_updated_by", null=True)
    updated = models.DateTimeField(default=datetime.now)

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(CaseMaster, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
