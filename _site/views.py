from django.shortcuts import render
from .sitehelper import build_params


def main(request):
    
    params = {
        "title": "Davide Wiest"
    }

    return render(request, "main.html", build_params("", ["en_main", "credentials", "projects"], params))
