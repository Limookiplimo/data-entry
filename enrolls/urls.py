from django.urls import path
from . import views

urlpatterns = [
    path("", views.enroll_employee, name="enroll")
]