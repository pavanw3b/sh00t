from django.test import TestCase
from .models import Project, Assessment


class ProjectModelTests(TestCase):
    new_project_name = "Project created by automated testing"
    new_flag_name = "Flag created by automated testing"
    new_sh0t_name = "Sh0t created by automated testing"
    new_assessment_name = "Assessment created by automated testing"

    def test_can_create_project(self):
        new_project = Project.objects.create(name=self.new_project_name)
        new_project.save()
        self.assertEqual(new_project.name, self.new_project_name)


    def test_can_create_assessment(self):
        new_project = Project.objects.create(name=self.new_project_name)
        new_project.save()

        new_assessment = Assessment.objects.create(name=self.new_assessment_name, project=new_project)
        new_assessment.save()
        self.assertEqual(new_assessment.name, self.new_assessment_name)

