from django.urls import path
from .views import home, operario,  auditor, superA, manejoProyecto, inforAuditor, usuarios


urlpatterns = [
    path('', home, name="home"),
    path('operario/', operario, name="operario"),
    path('auditor/', auditor, name="auditor"),
    path('superA/', superA, name="superA"),
    path('manejoProyecto/', manejoProyecto, name="manejoProyecto"),
    path('inforAuditor/', inforAuditor, name="inforAuditor"),
    path('usuarios/', usuarios, name="usuarios"),

  

]
