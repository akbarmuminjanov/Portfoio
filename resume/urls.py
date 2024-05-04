from django.urls import path
from .views import index, resume, portfolio, blog

urlpatterns = [
    path('', index, name="home"),
    path('resume/', resume, name="resume"),
    path('portfolio/', portfolio, name="portfolio"),
    path('blog/', blog, name="blog"),
]
