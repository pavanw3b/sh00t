from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Assessment, Project, Sh0t, Flag, Template
from configuration.models import ModuleMaster, CaseMaster
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
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


@login_required
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
    recent_flags = Flag.objects.all().order_by('added')

    context = {'assessments_list': assessments_list, 'recent_flags': recent_flags, 'submitted': submitted}

    return render(request, 'flags.html', context)


@login_required
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


@login_required
def sh0ts(request):
    submitted = ""
    if "POST" == request.method:
        title = request.POST.get('title', '')
        body = request.POST.get('body', '')
        assessment_id = request.POST.get('assessment', '')
        try:
            the_assessment = Assessment.objects.get(pk=assessment_id)
            new_sh0t = Sh0t.objects.create(title=title, body=body, assessment=the_assessment)
            new_sh0t.save()
            submitted = "success"
        except Assessment.DoesNotExist:
            return redirect('/')

    assessments_list = Assessment.objects.all()
    templates_list = Template.objects.all()
    recent_sh0ts = Sh0t.objects.all()
    context = {'assessments_list': assessments_list, 'templates': templates_list,
               'recent_sh0ts': recent_sh0ts, 'submitted': submitted}
    return render(request, 'sh0ts.html', context)


@login_required
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


@login_required
def assessments(request):
    submitted = ""
    if "POST" == request.method:
        name = request.POST.get('name', '')
        project_id = request.POST.get('project', '')
        try:
            the_project = Project.objects.get(pk=project_id)
            new_assessment = Assessment.objects.create(name=name, project=the_project)
            new_assessment.save()
            selected_modules = request.POST.getlist('modules')
            for module_id in selected_modules:
                module = ModuleMaster.objects.get(id=module_id)
                selected_cases = CaseMaster.objects.filter(module=module)
                for case in selected_cases:
                    note = "Module: " + module.name + "\n\n" + case.description
                    new_flag = Flag(title=case.name, note=note, assessment=new_assessment)
                    new_flag.save()
            submitted = "success"
        except Project.DoesNotExist:
            return redirect('/')
        except ModuleMaster.DoesNotExist:
            return redirect('/')
    assessments_list = Assessment.objects.all()
    modules_list = ModuleMaster.objects.all().order_by('order')
    cases_list = CaseMaster.objects.all().order_by('order')
    projects_list = Project.objects.all()
    context = {'assessments': assessments_list, 'projects': projects_list,
               'modules': modules_list, 'cases': cases_list, 'submitted': submitted}
    return render(request, 'assessments.html', context)


@login_required
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


@login_required
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


@login_required
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


@login_required
def templates(request):
    submitted = ""
    if "POST" == request.method:
        name = request.POST.get('name', '')
        body = request.POST.get('body', '')
        new_template = Template.objects.create(name=name, body=body)
        new_template.save()
        submitted = "success"
    templates_list = Template.objects.all()
    context = {'templates': templates_list, 'submitted': submitted}
    return render(request, 'templates.html', context)


@login_required
def template(request, template_id):
    submitted = ""
    try:
        the_template = Template.objects.get(pk=template_id)
        if "POST" == request.method:
            the_template.name = request.POST.get('name', '')
            the_template.body = request.POST.get('body', '')
            the_template.save()
            submitted = "success"
        context = {
            'template': the_template, 'submitted': submitted
        }
        return render(request, 'template-single.html', context)
    except Template.DoesNotExist:
        return redirect('/')


@login_required
def logout_user(request):
    logout(request)
    return redirect('/')
