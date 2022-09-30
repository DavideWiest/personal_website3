from django.urls import path
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from .sitehelper import openfile

def linkview(request, linkto):
    file = openfile("credentials.json", "links")
    if linkto not in file:
        return HttpResponseNotFound("Could not find this link")
    else:
        return redirect(file[linkto])



urlpatterns = [
    path("<str:linkto>", linkview)
]