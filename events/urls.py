from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.list_all, name="list"),
    path("create", views.create_event, name="create_event"),
]