from app.models import Project, Assessment, Sh0t, Flag, Template
from configuration.models import CaseMaster, ModuleMaster, MethodologyMaster
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'added')


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('name', 'added', 'project')


class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = ('id', 'title', 'note', 'done', 'assessment')


class Sh0tSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sh0t
        fields = ('title', 'severity', 'body', 'added', 'assessment')


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ('name', 'body')


class CaseMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseMaster
        fields = ('name', 'description', 'order', 'module')


class ModuleMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleMaster
        fields = ('name', 'description', 'order', 'methodology')


class MethodologyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodologyMaster
        fields = ('name', 'description', 'order')
