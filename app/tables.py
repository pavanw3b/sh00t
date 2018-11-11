import django_tables2 as tables
from .models import Project, Flag


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
    assessment = tables.TemplateColumn('<a href="/app/assessment/{{ record.assessment.pk}}"> '
                                       '{{ record.assessment }}</a>')

    class Meta:
        model = Flag
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'done', 'assessment', 'added')
        fields = ('name', 'added', 'done', 'assessment')


class OpenFlagTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    name = tables.TemplateColumn('<a href="/app/flag/{{ record.pk }}"> {{ record.title }}</a>')
    assessment = tables.TemplateColumn('<a href="/app/assessment/{{ record.assessment.pk}}"> '
                                       '{{ record.assessment }}</a>')

    class Meta:
        model = Flag
        template_name = "django_tables2/bootstrap-responsive.html"
        sequence = ('selection', 'name', 'assessment', 'added')
        fields = ('name', 'added', 'assessment')
