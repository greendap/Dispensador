from django.urls import path
from .views import home, operario,  auditor, superA, manejoProyecto, inforAuditor, usuarios, prueba
from Cables import views
"""
from django.conf import settings
from django.conf.urls.static import static
"""
urlpatterns = [
    path('', home, name="home"),
    path('operario/', operario, name="operario"),
    path('auditor/', auditor, name="auditor"),
    path('superA/', superA, name="superA"),
    path('manejoProyecto/', manejoProyecto, name="manejoProyecto"),
    path('inforAuditor/', inforAuditor, name="inforAuditor"),
    path('usuarios/', usuarios, name="usuarios"),
    path('prueba/', prueba, name="prueba"),
    path('crearproyectos/', views.crearproyectos),
    path('editarProyecto/<codigo>', views.editarProyecto),
    path('modificarProyecto/', views.modificarProyecto),
    path('prueba/eliminarProyecto/<codigo>', views.eliminarProyecto)

]
"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""