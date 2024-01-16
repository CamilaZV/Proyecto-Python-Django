from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home') ,
    path('home/', views.home, name='home'),
    path('registroUsuario/', views.registroUsuario, name='registroUsuario'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    path('gestionCursos/', views.gestionCursos, name='gestionCursos'),
    path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
    path('edicionCurso/<codigo>', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso, name='editarCurso'),
    path('eliminarCurso/<codigo>', views.eliminarCurso, name='eliminarCurso'),
    path('consultaCarreras/', views.consultaCarreras, name='consultaCarreras'),
    path('gestionEstudiantes/', views.gestionEstudiantes, name='gestionEstudiantes'),
    path('registrarEstudiante/', views.registrarEstudiante, name='registrarEstudiante'),
   
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reestablecer.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="reestablecer_enviado.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="reestablecer_confirma.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reestablecer_completo.html"), name='password_reset_complete'),
]