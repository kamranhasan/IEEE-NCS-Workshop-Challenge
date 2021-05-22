from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("contacted", views.contacted, name="contacted"),
    path("booked", views.booked, name="booked"),
    path("checked", views.checked, name="checked"),
]
