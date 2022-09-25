from django.urls import path
from django.http import FileResponse

def cv(request):
    return FileResponse(open('_site/static/resources/Lebenslauf.pdf', 'rb'), content_type='application/pdf')

def certificate(request):
    return FileResponse(open('_site/static/resources/Lebenslauf.pdf', 'rb'), content_type='application/pdf')




urlpatterns = [
    path("lebenslauf", cv),
    path("google-marketing-zertifikat", cv),
    # path("", views.main_log),
]