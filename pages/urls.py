from functools import update_wrapper
from django.urls import path

from . import views

urlpatterns = [
    path('<slug>', views.page, name="page"),

]