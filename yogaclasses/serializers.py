from rest_framework import serializers
from .models import Studio, Teacher, YogaClass

class YogaClassSerializer(serializers.HyperlinkedModelSerializer):
    studio = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()
    
    class Meta:
        model = YogaClass
        fields = ('url', 'studio', 'teacher', 'description', 'date', 'start_time', 'end_time')

class StudioSerializer(serializers.HyperlinkedModelSerializer):
    yoga_classes = YogaClassSerializer(many=True, read_only=True)

    class Meta:
        model = Studio
        fields = ('url', 'pk', 'name', 'yoga_classes')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    yoga_classes = YogaClassSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ('url', 'pk', 'name', 'yoga_classes')   

