from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("<str:lang_choice>", views.main)
    # path("", views.main_log),
]