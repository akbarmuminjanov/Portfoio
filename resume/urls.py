from django.urls import path
from .views import Home, Resume

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('resume/', Resume.as_view(), name="resume")
]
