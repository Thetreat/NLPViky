from django.urls import path

from . import views

urlpatterns = [
    path("", views.mo1, name='index'),
    path("mo1", views.mo1, name="mo1"),
    path("mo2", views.mo2, name="mo2"),
    path("mo3", views.mo3, name="mo3"),
    path("mo4", views.mo4, name="mo4"),
    path("mo5", views.mo5, name="mo5"),
]