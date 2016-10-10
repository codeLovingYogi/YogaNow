from django.shortcuts import render
from .models import Studio, Teacher, YogaClass
from .serializers import StudioSerializer, TeacherSerializer, YogaClassSerializer
from rest_framework import viewsets, permissions

def index(request):
    yogaclasses = YogaClass.objects.all()
    return render(request, 'yogaclasses/index.html', {'yogaclasses': yogaclasses})

class StudioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Studios to be viewed or edited.
    """
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Teachers to be viewed or edited.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class YogaClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Studios to be viewed or edited.
    """
    queryset = YogaClass.objects.all()
    serializer_class = YogaClassSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)