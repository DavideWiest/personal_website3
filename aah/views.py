from django.shortcuts import render
from _site.base import build_params, choose_lang, handle_requestdata, allowed_languages



def aah_main(request):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)

    params = {"title": "AAAAaahhhhh"}
    
    return render(request, "aah_main.html", build_params("", ["main"], params, l))
