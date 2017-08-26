# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Assessment, Sh0t, Flag


class FlagAdmin(admin.ModelAdmin):
    list_display = ('title', 'assessment', 'added')

admin.site.register(Project)
admin.site.register(Assessment)

admin.site.register(Sh0t)
admin.site.register(Flag, FlagAdmin)

