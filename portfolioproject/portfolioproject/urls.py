"""
URL configuration for portfolioproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
# Importa el objeto 'settings' de django.conf para acceder a la configuración del proyecto.

from django.conf.urls.static import static
# Importa la función 'static' de django.conf.urls.static para servir archivos estáticos y de medios en modo de depuración.

from django.contrib import admin
# Importa el módulo 'admin' de django.contrib para habilitar la administración del sitio.

from django.urls import path, include
# Importa las funciones 'path' e 'include' de django.urls para definir rutas URL y incluir otras configuraciones de URLs.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ruta para la interfaz de administración de Django.
    # URL: 'admin/', vista: 'admin.site.urls'.

    path('', include('myportfolio.urls')),
    # Incluye las rutas URL de la aplicación 'myportfolio'.
    # URL: '', incluye: 'myportfolio.urls'.
    path('accounts/', include('django.contrib.auth.urls')),  # Añade las vistas de autenticación de Django
    ###Etapa 5
    path('ckeditor', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    # Condicional para verificar si el modo de depuración está habilitado.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Si el modo de depuración está habilitado, añade las rutas para servir archivos de medios.
    # URL base: settings.MEDIA_URL, directorio raíz de documentos: settings.MEDIA_ROOT.
