from django.shortcuts import render

from .models import Resume

# Create your views here.
def index(request):
    resume = Resume.objects.all()
    return render(request, "index.html", {"resume":resume})

def resume(request):
    return render(request, "resume.html")
