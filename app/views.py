from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Assessment, Project, Sh0t, Flag


def index(request):
    open_flags = Flag.objects.filter(done=False)
    recent_flags = Flag.objects.all()
    recent_sh0ts = Sh0t.objects.all()
    assessments_count = Assessment.objects.all().count()
    projects_count = Project.objects.all().count()

    context = {
        'open_flags': open_flags,
        'recent_flags': recent_flags,
        'recent_sh0ts': recent_sh0ts,
        'assessments_count': assessments_count,
        'projects_count': projects_count,
    }
    return render(request, 'index.html', context)


def flags(request):
    submitted = ""
    if "POST" == request.method:
        title = request.POST.get('title', '')
        note = request.POST.get('note', '')
        assessment_id = request.POST.get('assessment', '')
        if "done" == request.POST.get('done', ''):
            done = True
        else:
            done = False
        try:
            assessment = Assessment.objects.get(pk=assessment_id)
            new_flag = Flag.objects.create(title=title, note=note, assessment=assessment, done=done)
            new_flag.save()
            submitted = "success"
        except Assessment.DoesNotExist:
            return redirect('/')

    assessments_list = Assessment.objects.all()
    recent_flags = Flag.objects.all()

    context = {'assessments_list': assessments_list, 'recent_flags': recent_flags, 'submitted': submitted}

    return render(request, 'flags.html', context)


def flag(request, flag_id):
    submitted = ""
    try:
        the_flag = Flag.objects.get(pk=flag_id)

        if "POST" == request.method:
            assessment_id = request.POST.get('assessment', '')
            try:
                the_flag.title = request.POST.get('title', '')
                the_flag.note = request.POST.get('note', '')
                if "done" == request.POST.get('done', ''):
                    the_flag.done = True
                else:
                    the_flag.done = False
                the_flag.assessment = Assessment.objects.get(pk=assessment_id)
                the_flag.save()
                submitted = "success"
            except Assessment.DoesNotExist:
                return redirect('/')

        assessments = Assessment.objects.all()
        context = {'flag': the_flag, 'assessments': assessments, 'submitted': submitted}
        return render(request, 'flag-single.html', context)
    except Flag.DoesNotExist:
        return redirect('/')


def sh0ts(request):
    submitted = ""
    if "POST" == request.method:
        title = request.POST.get('title', '')
        body = request.POST.get('body', '')
        assessment_id = request.POST.get('assessment', '')
        try:
            assessment = Assessment.objects.get(pk=assessment_id)
            new_sh0t = Sh0t.objects.create(title=title, body=body, assessment=assessment)
            new_sh0t.save()
            submitted = "success"
        except Assessment.DoesNotExist:
            return redirect('/')

    assessments_list = Assessment.objects.all()
    recent_sh0ts = Sh0t.objects.all()
    context = {'assessments_list': assessments_list, 'recent_sh0ts': recent_sh0ts, 'submitted': submitted}
    return render(request, 'sh0ts.html', context)


def sh0t(request, flag_id):
    submitted = ""
    try:
        the_sh0t = Sh0t.objects.get(pk=flag_id)

        if "POST" == request.method:
            assessment_id = request.POST.get('assessment', '')
            try:
                the_sh0t.title = request.POST.get('title', '')
                the_sh0t.body = request.POST.get('body', '')
                the_sh0t.assessment = Assessment.objects.get(pk=assessment_id)
                the_sh0t.save()
                submitted = "success"
            except Assessment.DoesNotExist:
                return redirect('/')

        assessments = Assessment.objects.all()
        context = {'sh0t': the_sh0t, 'assessments': assessments, 'submitted': submitted}
        return render(request, 'sh0t-single.html', context)
    except Flag.DoesNotExist:
        return redirect('/')
