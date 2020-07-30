from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from main import views as main_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('.<str:suffix>/', main_views.url_redirect, name="url_redirect")

]
