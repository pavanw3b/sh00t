# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import CaseMaster, ModuleMaster, MethodologyMaster


class MethodologyMasterAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'order']
    list_display = ['name', 'description', 'order', 'created', 'updated']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']


class ModuleMasterAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'methodology',  'order']
    list_display = ['name', 'description', 'methodology', 'order', 'created', 'updated']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']


class CaseMasterAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'module', 'order']
    list_display = ['name', 'description', 'module', 'get_methodology', 'order', 'created', 'updated']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']

    def get_methodology(self, case):
        return case.module.methodology


admin.site.register(MethodologyMaster, MethodologyMasterAdmin)
admin.site.register(ModuleMaster, ModuleMasterAdmin)
admin.site.register(CaseMaster, CaseMasterAdmin)
