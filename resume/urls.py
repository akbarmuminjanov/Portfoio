from django.urls import path
from .views import index, resume

urlpatterns = [
    path('', index, name="home"),
    path('resume/', resume, name="resume")
]
