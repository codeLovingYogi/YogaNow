from django.contrib import admin
from .models import Studio
from .models import Teacher
from .models import YogaClass

admin.site.register(Studio)
admin.site.register(Teacher)
admin.site.register(YogaClass)
