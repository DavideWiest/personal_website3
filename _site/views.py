from django.http import HttpResponseNotFound
from django.shortcuts import render
from .base import build_params, choose_lang, handle_requestdata, allowed_languages, openContentFile
from .projectsUtil import categoriesByReferenceCountWithBrightness, technologiesByReferenceCountWithBrightness


def main(request):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)
    
    params = {
        "title": "Davide Wiest",
        "skillsInfo": {
            "categoriesData": categoriesByReferenceCountWithBrightness(12),
            "technologiesData": technologiesByReferenceCountWithBrightness(12)
        }
    }

    return render(request, "main.html", build_params("", ["main", "credentials", "projects", "skills_knowledge_content"], params, l))

def projects(request):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)

    params = {
        "filter_category": request.GET.get("category", None),
        "filter_technology": request.GET.get("technology", None)
    }

    return render(request, "projects.html", build_params("Projekte", ["credentials", "projects", "projects_content"], params, l))
