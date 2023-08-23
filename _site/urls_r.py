<<<<<<< HEAD
from django.urls import path
from django.http import FileResponse
from django.http import HttpResponseNotFound

from .base import choose_lang

def other(request, resource_title):
    try:
        return FileResponse(open(f'_site/static/resources/{resource_title}', 'rb'), content_type='application/pdf')
    except:
        return HttpResponseNotFound("This file does not exist.")

urlpatterns = [
    path("<str:resource_title>", other)
=======
from django.urls import path
from django.http import FileResponse
from django.http import HttpResponseNotFound

from .base import choose_lang

def other(request, resource_title):
    try:
        return FileResponse(open(f'_site/static/resources/{resource_title}', 'rb'), content_type='application/pdf')
    except:
        return HttpResponseNotFound("This file does not exist.")

urlpatterns = [
    path("<str:resource_title>", other)
>>>>>>> 8f772811bbf909d83ef59f27f656476037510343
]