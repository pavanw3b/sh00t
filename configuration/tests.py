# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import MethodologyMaster, ModuleMaster, CaseMaster

class ModelTests(TestCase):
    new_methodology_name = "Methodology created by automated testing"
    new_module_name = "Module created by automated testing"
    new_case_name = "Case created by automated testing"

    def __create_a_methodology(self):
        new_methodology = MethodologyMaster.objects.create(name=self.new_methodology_name)
        return new_methodology

    def __create_a_module(self):
        new_methodology = self.__create_a_methodology()
        new_module = ModuleMaster.objects.create(name=self.new_module_name, methodology=new_methodology)
        new_module.save()
        return new_module

    def __create_a_case(self):
        new_module = self.__create_a_module()
        new_case = CaseMaster.objects.create(name=self.new_case_name, module=new_module)
        return new_case

    def test_can_create_methodology(self):
        new_methodology = self.__create_a_methodology()
        self.assertEqual(new_methodology.name, self.new_methodology_name)

    def test_can_create_module(self):
        new_module = self.__create_a_module()
        self.assertEqual(new_module.name, self.new_module_name)

    def test_can_create_case(self):
        new_case = self.__create_a_case()
        self.assertEqual(new_case.name, self.new_case_name)
