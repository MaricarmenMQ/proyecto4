
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Hola, name="index"),
    path("datos", views.datos_personales, name="datos"),
    path("preferencias", views.preferencias, name="preferencias"),
    path("gustos", views.gustos, name="gustos"),
    path("habilidades", views.habilidades, name="habilidades"),
    path("familia", views.familia, name="familia"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

