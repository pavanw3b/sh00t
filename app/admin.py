# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Assessment, Sh0t, Flag, Template


class FlagAdmin(admin.ModelAdmin):
    list_display = ('title', 'assessment', 'added', 'order')


admin.site.register(Project)
admin.site.register(Assessment)

admin.site.register(Sh0t)
admin.site.register(Flag, FlagAdmin)
admin.site.register(Template)
