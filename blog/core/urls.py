from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('profesores/<int:pk>/', views.detalle_profesor, name='detalle_profesor'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:pk>/', views.detalle_curso, name='detalle_curso'),
]