from django.shortcuts import render
from django.http import HttpResponse
from .sitehelper import build_params


def main(request):
    
    params = {
        "title": "Davide Wiest"
    }

    return render(request, "main.html", build_params("", params))
