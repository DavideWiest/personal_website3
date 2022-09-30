from django.shortcuts import render
from .sitehelper import build_params, choose_lang



def main(request):
    
    params = {
        "title": "Davide Wiest"
    }
    
    l = choose_lang(request)
    return render(request, "main.html", build_params("", [f"main", "credentials", f"projects"], params, l))
