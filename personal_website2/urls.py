"""personal_website2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class StaticViewSitemap(Sitemap):
    def items(self):
        return ["views.main"]
    def location(self, item):
        return reverse(item)

@require_GET
def robots_txt(request, lang_choice=None):
    lines = [
        "User-Agent: *",
        "Allow: /",
        "Sitemap: https://davidewiest.com/sitemap.txt"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

@require_GET
def sitemap_txt(request):
    lines = [
        "https://davidewiest.com/",
        "https://davidewiest.com/robots.txt",
        "https://davidewiest.com/sitemap.txt"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('_site.urls')),
    path('', include('_site.urls_legal')),
    path('aah/', include('aah.urls')),
    path('ressourcen/', include('_site.urls_r')),
    path('resources/', include('_site.urls_r')),
    path('link/', include('_site.urls_l')),
    path('robots.txt', robots_txt),
    path("sitemap.txt", sitemap_txt)
]
