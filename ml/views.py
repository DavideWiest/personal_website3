from django.shortcuts import render
from _site.base import build_params, choose_lang, handle_requestdata, allowed_languages



def main(request):
    l = choose_lang(request)
    request.session = handle_requestdata(request, l)
    