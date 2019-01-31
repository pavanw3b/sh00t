import django_tables2 as tables
from .models import Project, Flag, Sh0t, Assessment, Project


class ProjectTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/project/{{ record.pk }}"> {{ record.name }}</a>')

    class Meta:
        model = Project
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'added')
        fields = ('name', 'added')


class FlagTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/flag/{{ record.pk }}"> {{ record.title }}</a>')
    done = tables.BooleanColumn(yesno='done,')
    project = tables.TemplateColumn('<a href="/app/project/{{ record.assessment.project.pk}}">{{ record.assessment.project }}</a>')
    assessment = tables.TemplateColumn('<a href="/app/assessment/{{ record.assessment.pk}}"> '
                                       '{{ record.assessment }}</a>')

    class Meta:
        model = Flag
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'done', 'project', 'assessment', 'added')
        fields = ('name', 'added', 'done', 'project', 'assessment')
        empty_text = "No Flags yet"


class OpenFlagTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/flag/{{ record.pk }}"> {{ record.title }}</a>')
    project = tables.TemplateColumn('<a href="/app/project/{{ record.assessment.project.pk}}">{{ record.assessment.project }}</a>')
    assessment = tables.TemplateColumn('<a href="/app/assessment/{{ record.assessment.pk}}"> '
                                       '{{ record.assessment }}</a>')

    class Meta:
        model = Flag
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'project', 'assessment', 'added')
        fields = ('name', 'added', 'project', 'assessment')


class Sh0tTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    severity = tables.TemplateColumn('<span class="bc-badge bc-badge--p{{ record.severity }}">P{{ record.severity }}</span>')
    title = tables.TemplateColumn('<a href="/app/sh0t/{{ record.pk }}">{{ record.title }}</a>')
    project = tables.TemplateColumn('<a href="/app/project/{{ record.assessment.project.pk}}">{{ record.assessment.project }}</a>')
    assessment = tables.TemplateColumn('<a href="/app/assessment/{{ record.assessment.pk}}">{{ record.assessment }}</a>')

    class Meta:
        model = Sh0t
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection','severity', 'title', 'project', 'assessment', 'added')
        fields = ('severity', 'title', 'project', 'assessment', 'added')


class AssessmentTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/assessment/{{ record.pk }}"> {{ record.name }}</a>')
    project = tables.TemplateColumn('<a href="/app/project/{{ record.project.pk}}"> '
                                       '{{ record.project }}</a>')

    class Meta:
        model = Assessment
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'project', 'added')
        fields = ('name', 'project', 'added')

