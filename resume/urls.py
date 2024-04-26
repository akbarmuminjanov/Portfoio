from django.urls import path
from .views import index, resume, base

urlpatterns = [
    path('', base, name="base"),
    path('index/', index, name="home"),
    path('resume/', resume, name="resume")
]
