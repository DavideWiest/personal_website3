from django.urls import path
from django.http import FileResponse
from django.http import HttpResponseNotFound

from .base import choose_lang

def cv(request):
    l = choose_lang(request)
    if l == "de":
        return FileResponse(open('_site/static/resources/Lebenslauf.pdf', 'rb'), content_type='application/pdf')
    else:
        return FileResponse(open('_site/static/resources/CV.pdf', 'rb'), content_type='application/pdf')

def other(request, resource_title):
    try:
        return FileResponse(open(f'_site/static/resources/{resource_title}', 'rb'), content_type='application/pdf')
    except:
        return HttpResponseNotFound("This file does not exist.")

urlpatterns = [
    path("cv", cv),
    path("<str:resource_title>", other)
]