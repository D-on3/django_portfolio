from django.urls import path
from .views import *


urlpatterns = [
    path("", home,name="home"),
    path("gabrovo/", show_gabrovo, name="gabrovo"),
    path("sofia/", show_sofia, name="sofia"),
    path("varna/", show_varna, name="varna")
]
