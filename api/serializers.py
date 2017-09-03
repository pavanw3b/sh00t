from app.models import Flag
from rest_framework import serializers


class FlagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flag
        fields = ('title', 'note', 'done', 'added')
