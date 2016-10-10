from rest_framework import serializers
from .models import Studio, Teacher, YogaClass

class StudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studio
        fields = ('url', 'pk', 'name')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'pk', 'name')

class YogaClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YogaClass
        fields = ('url', 'studio', 'teacher', 'description', 'date', 'start_time', 'end_time')