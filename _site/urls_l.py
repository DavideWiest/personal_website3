from django.urls import path
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from .base import openContentFile

def linkview(request, linkto):
    file = openContentFile("credentials.json", "links")
    if linkto not in file:
        return HttpResponseNotFound("Could not find this link")
    else:
        return redirect(file[linkto])



urlpatterns = [
    path("<str:linkto>", linkview)
]