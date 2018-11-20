# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from app.models import Template
from .serializers import FlagSerializer, Sh0tSerializer, AssessmentSerializer, ProjectSerializer, TemplateSerializer
from .serializers import CaseMasterSerializer, ModuleMasterSerializer, MethodologyMasterSerializer
from app.models import Flag, Sh0t, Assessment, Project
from configuration.models import CaseMaster, ModuleMaster, MethodologyMaster
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def flag_detail(request, pk):
    try:
        flag = Flag.objects.get(pk=pk)
    except Flag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlagSerializer(flag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FlagSerializer(flag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = FlagSerializer(flag, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def flag_list(request):
    if request.method == 'GET':
        flags = Flag.objects.all()
        serializer = FlagSerializer(flags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FlagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def sh0t_detail(request, pk):
    try:
        sh0t = Sh0t.objects.get(pk=pk)
    except Sh0t.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Sh0tSerializer(sh0t)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Sh0tSerializer(sh0t, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sh0t.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def sh0t_list(request):
    if request.method == 'GET':
        flags = Sh0t.objects.all()
        serializer = Sh0tSerializer(flags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Sh0tSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def assessment_detail(request, pk):
    try:
        assessment = Assessment.objects.get(pk=pk)
    except Assessment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AssessmentSerializer(assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def assessment_list(request):
    if request.method == 'GET':
        assessments = Assessment.objects.all()
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def template_detail(request, pk):
    try:
        template = Template.objects.get(pk=pk)
    except Template.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TemplateSerializer(template)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TemplateSerializer(template, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        template.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def template_list(request):
    if request.method == 'GET':
        templates = Template.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def case_master_detail(request, pk):
    try:
        case_master = CaseMaster.objects.get(pk=pk)
    except CaseMaster.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CaseMasterSerializer(case_master)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CaseMasterSerializer(case_master, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        case_master.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def case_master_list(request):
    if request.method == 'GET':
        case_masters = CaseMaster.objects.all()
        serializer = CaseMasterSerializer(case_masters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CaseMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def module_master_detail(request, pk):
    try:
        module_master = ModuleMaster.objects.get(pk=pk)
    except ModuleMaster.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ModuleMasterSerializer(module_master)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ModuleMasterSerializer(module_master, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        module_master.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def module_master_list(request):
    if request.method == 'GET':
        module_master = ModuleMaster.objects.all()
        serializer = ModuleMasterSerializer(module_master, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ModuleMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def methodology_master_detail(request, pk):
    try:
        methodology_master = MethodologyMaster.objects.get(pk=pk)
    except ModuleMaster.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MethodologyMasterSerializer(methodology_master)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MethodologyMasterSerializer(methodology_master, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        methodology_master.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def methodology_master_list(request):
    if request.method == 'GET':
        module_master = MethodologyMaster.objects.all()
        serializer = MethodologyMasterSerializer(module_master, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MethodologyMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

