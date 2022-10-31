from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("projects", views.projects),
    path("projects/<str:project>", views.projects),
]