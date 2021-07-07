from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'studenti', StudentViewSet)
router.register(r'profesori', ProfesorViewSet)

urlpatterns = [
    path("" , homepage, name = "homepage"),
    path("studenti" , StudentList.as_view()),
    path("profesori" , ProfesorList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]