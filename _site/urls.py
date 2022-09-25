from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    # path("", views.stdout_log),
    # path("", views.main_log),
]