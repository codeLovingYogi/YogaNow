from django.conf.urls import include, url
from django.contrib import admin
from . import views
from rest_framework import routers

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'studios', views.StudioViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'yogaclasses', views.YogaClassViewSet)

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]