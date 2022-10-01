from django.urls import path
from django.http import FileResponse
from django.http import HttpResponseNotFound


def de_cv(request):
    return FileResponse(open('_site/static/resources/Lebenslauf.pdf', 'rb'), content_type='application/pdf')

def en_cv(request):
    return FileResponse(open('_site/static/resources/CV.pdf', 'rb'), content_type='application/pdf')

def de_certificate(request):
    return FileResponse(open('_site/static/resources/Zertifikat_Google.pdf', 'rb'), content_type='application/pdf')

def en_certificate(request):
    return FileResponse(open('_site/static/resources/Certificate_Google.pdf', 'rb'), content_type='application/pdf')

def other(request, resource_title):
    try:
        return FileResponse(open(f'_site/static/resources/{resource_title}', 'rb'), content_type='application/pdf')
    except:
        return HttpResponseNotFound("This file does not exist.")



urlpatterns = [
    path("lebenslauf", de_cv),
    path("google-marketing-zertifikat", de_certificate),
    path("cv", en_cv),
    path("google-marketing-certificate", en_certificate),
    path("<str:resource_title>", other)
    # path("", views.main_log),
]