# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Assessment, Case, Module

admin.site.register(Project)
admin.site.register(Assessment)
admin.site.register(Case)
admin.site.register(Module)