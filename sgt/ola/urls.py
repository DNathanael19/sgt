from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index"),
               #path("greet", views.greet, name="greet"),
               #path("<str:nome>", views.saudacao, name="index1"),
               #path("<str:nome>", views.greet, name="")
               path("", views.tia_do_zap, name="tia_do_zap")]