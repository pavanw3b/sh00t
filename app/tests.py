from django.test import TestCase
from .models import Project, Assessment, Sh0t, Flag, Template


class ModelTests(TestCase):
    new_project_name = "Project created by automated testing"
    new_flag_name = "Flag created by automated testing"
    new_sh0t_name = "Sh0t created by automated testing"
    new_assessment_name = "Assessment created by automated testing"
    new_template_name = "Template created by automated testing"
    new_template_body = ""

    def __create_a_project(self):
        new_project = Project.objects.create(name=self.new_project_name)
        return new_project

    def __create_an_assessment(self):
        new_project = self.__create_a_project()
        new_assessment = Assessment.objects.create(name=self.new_assessment_name, project=new_project)
        new_assessment.save()
        return new_assessment

    def __create_a_flag(self):
        new_assessment = self.__create_an_assessment()
        new_flag = Flag.objects.create(title=self.new_flag_name, assessment=new_assessment)
        return new_flag

    def __create_a_sh0t(self):
        new_assessment = self.__create_an_assessment()
        new_sh0t = Sh0t.objects.create(title=self.new_sh0t_name, assessment=new_assessment)
        return new_sh0t

    def __create_a_template(self):
        new_template = Template.objects.create(name=self.new_template_name, body=self.new_template_body)
        new_template.save()
        return  new_template

    def test_can_create_project(self):
        new_project = self.__create_a_project()
        self.assertEqual(new_project.name, self.new_project_name)

    def test_can_create_assessment(self):
        new_assessment = self.__create_an_assessment()
        self.assertEqual(new_assessment.name, self.new_assessment_name)

    def test_can_create_flag(self):
        new_flag = self.__create_a_flag()
        self.assertEqual(new_flag.title, self.new_flag_name)

    def test_can_create_sh0t(self):
        new_sh0t = self.__create_a_sh0t()
        self.assertEqual(new_sh0t.title, self.new_sh0t_name)

    def test_can_create_template(self):
        new_template = self.__create_a_template()
        self.assertEqual(new_template.name, self.new_template_name)
        self.assertEqual(new_template.body, self.new_template_body)
