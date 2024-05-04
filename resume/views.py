from django.shortcuts import render

from .models import Resume

# Create your views here.
def index(request):
    resume = Resume.objects.get()
    return render(request, "index.html", {"resume":resume})

def resume(request):
    resume = Resume.objects.get()
    return render(request, "resume.html", {"resume":resume})

def portfolio(request):
    resume = Resume.objects.get()
    return render(request, "portfolio.html", {"resume":resume})

def blog(request):
    resume = Resume.objects.get()
    return render(request, "blog.html", {"resume":resume})