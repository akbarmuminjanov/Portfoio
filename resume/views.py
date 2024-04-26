from django.shortcuts import render

from .models import Resume

# Create your views here.
def base(request):
    resume = Resume.objects.all()
    return render(request, "base.html", {"resume":resume})

def index(request):
    return render(request, "index.html")

def resume(request):
    return render(request, "resume.html")
