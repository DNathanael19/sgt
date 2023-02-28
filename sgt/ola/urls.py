from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index2"),
               path("<str:nome>", views.saudacao, name="saudacao")]