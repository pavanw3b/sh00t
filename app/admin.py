# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Assessment, Sh0t, Flag

admin.site.register(Project)
admin.site.register(Assessment)

admin.site.register(Sh0t)
admin.site.register(Flag)
