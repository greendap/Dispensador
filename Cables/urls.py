from django.urls import path
from .views import home, operario


urlpatterns = [
    path('', home, name="home"),
    path('operario/', operario, name="operario"),
]
