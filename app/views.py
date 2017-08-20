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
            the_assessment = Assessment.objects.get(pk=assessment_id)
            new_flag = Flag.objects.create(title=title, note=note, assessment=the_assessment, done=done)
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

        assessments_list = Assessment.objects.all()
        context = {'flag': the_flag, 'assessments': assessments_list, 'submitted': submitted}
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


def sh0t(request, sh0t_id):
    submitted = ""
    try:
        the_sh0t = Sh0t.objects.get(pk=sh0t_id)

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

        assessments_list = Assessment.objects.all()
        context = {'sh0t': the_sh0t, 'assessments': assessments_list, 'submitted': submitted}
        return render(request, 'sh0t-single.html', context)
    except sh0t.DoesNotExist:
        return redirect('/')


def assessments(request):
    submitted = ""
    if "POST" == request.method:
        name = request.POST.get('name', '')
        project_id = request.POST.get('project', '')
        try:
            the_project = Project.objects.get(pk=project_id)
            new_assessment = Assessment.objects.create(name=name, project=the_project)
            new_assessment.save()
            submitted = "success"
        except Project.DoesNotExist:
            return redirect('/')
    assessments_list = Assessment.objects.all()
    projects_list = Project.objects.all()
    context = {'assessments': assessments_list, 'projects': projects_list, 'submitted': submitted}
    return render(request, 'assessments.html', context)


def assessment(request, assessment_id):
    submitted = ""
    try:
        the_assessment = Assessment.objects.get(pk=assessment_id)
        if "POST" == request.method:
            project_id = request.POST.get('project', '')
            try:
                the_assessment.name = request.POST.get('name', '')
                the_assessment.project = Project.objects.get(pk=project_id)
                the_assessment.save()
                submitted = "success"
            except Project.DoesNotExist:
                return redirect('/')
        recent_assessments = Assessment.objects.all()
        projects_list = Project.objects.all()
        context = {
            'assessment': the_assessment, 'recent_assessments': recent_assessments, 'projects': projects_list,
            'submitted': submitted
        }
        return render(request, 'assessment-single.html', context)
    except Assessment.DoesNotExist:
        return redirect('/')


def projects(request):
    submitted = ""
    if "POST" == request.method:
        name = request.POST.get('name', '')
        new_project = Project.objects.create(name=name)
        new_project.save()
        submitted = "success"
    projects_list = Project.objects.all()
    context = {'projects': projects_list, 'submitted': submitted}
    return render(request, 'projects.html', context)


def project(request, project_id):
    submitted = ""
    try:
        the_project = Project.objects.get(pk=project_id)
        if "POST" == request.method:
            the_project.name = request.POST.get('name', '')
            the_project.save()
            submitted = "success"
        context = {
            'project': the_project, 'submitted': submitted
        }
        return render(request, 'project-single.html', context)
    except Project.DoesNotExist:
        return redirect('/')
