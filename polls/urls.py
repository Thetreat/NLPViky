from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("mo5", views.mo5, name="mo5"),
]