from django.shortcuts import render
from _site.base import build_params, choose_lang, handle_requestdata, allowed_languages



def main(request):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)

    params = {"title": "Hello World"}
    
    return render(request, "main.html", build_params("", ["main", "credentials", "projects"], params, l, base_path="ml"))
