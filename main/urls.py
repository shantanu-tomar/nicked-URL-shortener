from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('shorten/', views.url_shortener, name="shorten"),
]
