from django.http import Http404
from django.shortcuts import render
from .base import build_params, choose_lang, handle_requestdata, allowed_languages, openfile



def main(request):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)
    
    params = {
        "title": "Davide Wiest"
    }
    
    return render(request, "main.html", build_params("", ["main", "credentials", "projects"], params, l))

def projets(request, project=None):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)
    
    params = {}

    projects = openfile(l + "_projects.json")["projects"]

    if project == None:
        return render(request, "projects.html", build_params("Projekte", ["credentials", "projects"], params, l))
    elif project in list(projects):
        return render(request, "singleproject.html", build_params("Projekte", ["credentials", "projects"], params, l))
    else:
        return Http404


