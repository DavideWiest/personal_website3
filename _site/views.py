from django.http import HttpResponseNotFound
from django.shortcuts import render
from .base import build_params, choose_lang, handle_requestdata, allowed_languages, openfile



def main(request):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)
    
    params = {
        "title": "Davide Wiest"
    }
    
    return render(request, "main.html", build_params("", ["main", "credentials", "projects"], params, l))

def projects(request):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)
    
    params = {}

    return render(request, "projects.html", build_params("Projekte", ["credentials", "projects"], params, l))
