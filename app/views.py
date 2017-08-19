from __future__ import unicode_literals
from django.shortcuts import render
from .models import Assessment, Flag


def index(request):
    context = {}
    return render(request, 'index.html', context)


def flag(request):
    if "POST" == request.method:
        title = request.POST.get('title', '')
        note = request.POST.get('note', '')
        new_flag = Flag.objects.create(title=title, note=note)
        new_flag.save()
    assessments = Assessment.objects.all()
    flags = Flag.objects.all()

    context = {'assessments': assessments, 'flags': flags}

    return render(request, 'flags.html', context)
