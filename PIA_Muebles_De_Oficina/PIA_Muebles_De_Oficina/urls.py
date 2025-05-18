from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # 👈 Agrega esto

# 👇 Define una vista básica
def inicio(request):
    return HttpResponse("Sitio de muebles de oficina!")

# 👇 Agrega la nueva vista a las rutas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),  # 👈 Esta línea es clave
]
