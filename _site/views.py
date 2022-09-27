from django.shortcuts import render
from .sitehelper import build_params


def main(request):
    
    params = {
        "title": "Davide Wiest"
    }

    return render(request, "main.html", build_params("", "", params))

def projects(request):
    
    params = {
        "title": "Davide Wiest"
    }

    return render(request, "project.html", build_params("Projekte", "data.json/projects", params))
