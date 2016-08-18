from django.shortcuts import render
from .models import Studio
from .models import Teacher
from .models import YogaClass

def index(request):
    yogaclasses = YogaClass.objects.all()
    return render(request, 'yogaclasses/index.html', {'yogaclasses': yogaclasses})

