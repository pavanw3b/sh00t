# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app.models import Template
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def template(request, template_id):
    response = {}
    try:
        the_template = Template.objects.get(pk=template_id)
        response['status'] = 200
        response['name'] = the_template.name
        response['body'] = the_template.body
    except Template.DoesNotExist:
        response['status'] = 404
    return JsonResponse(response)
