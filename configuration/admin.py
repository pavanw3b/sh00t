# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import CaseMaster, ModuleMaster


class ModuleMasterAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'order']
    list_display = ['name', 'description', 'order', 'created', 'updated']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']


class CaseMasterAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'module', 'order']
    list_display = ['name', 'description', 'order', 'created', 'updated']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']


admin.site.register(ModuleMaster, ModuleMasterAdmin)
admin.site.register(CaseMaster, CaseMasterAdmin)
