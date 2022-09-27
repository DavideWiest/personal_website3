from django.urls import path
from django.http import FileResponse

def de_cv(request):
    return FileResponse(open('_site/static/resources/Lebenslauf.pdf', 'rb'), content_type='application/pdf')

def en_cv(request):
    return FileResponse(open('_site/static/resources/CV.pdf', 'rb'), content_type='application/pdf')

def de_certificate(request):
    return FileResponse(open('_site/static/resources/Zertifikat_Google.pdf', 'rb'), content_type='application/pdf')

def en_certificate(request):
    return FileResponse(open('_site/static/resources/Certificate_Google.pdf', 'rb'), content_type='application/pdf')




urlpatterns = [
    path("lebenslauf", de_cv),
    path("google-marketing-zertifikat", de_certificate),
    path("cv", en_cv),
    path("google-marketing-certificate", en_certificate),
    # path("", views.main_log),
]