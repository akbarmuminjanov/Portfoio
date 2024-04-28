from django.shortcuts import render

from .models import Resume

# Create your views here.
def index(request):
    resume = Resume.objects.get()
    return render(request, "index.html", {"resume":resume})

def resume(request):
    resume = Resume.objects.get()
    return render(request, "resume.html", {"resume":resume})
