from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="inicio"),
    path("crear/", views.crear, name="crear"),
    path("borrar/<int:nota_id>/", views.borrar, name="borrar"),
    path("modificar/<int:nota_id>/", views.modificar, name="modificar"),
]