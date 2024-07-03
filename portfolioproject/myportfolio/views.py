# Importa decoradores y funciones útiles para la autenticación y manejo de vistas
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Importa el formulario de contacto y los modelos Proyecto y Contacto de la aplicación actual
from .forms import ContactoForm
from .models import Proyecto, Contacto

# Vista para la página de inicio que muestra los proyectos
def index(request):
    # Obtiene todos los objetos de la clase Proyecto
    proyectos = Proyecto.objects.all()
    # Renderiza la plantilla 'index.html' pasando los proyectos como contexto
    return render(request, 'index.html', {'proyectos': proyectos})

# Vista para crear un nuevo contacto usando un formulario
def contacto_nuevo(request):
    # Si la solicitud es de tipo POST, se procesa el formulario
    if request.method == "POST":
        # Se crea una instancia del formulario con los datos enviados
        form = ContactoForm(request.POST)
        # Si el formulario es válido, se guarda el nuevo contacto
        if form.is_valid():
            form.save()
            # Redirige a una página de confirmación
            return redirect('contacto_confirmacion')
    else:
        # Si la solicitud no es POST, se crea un formulario vacío
        form = ContactoForm()
    # Renderiza la plantilla 'contacto_formulario.html' pasando el formulario como contexto
    return render(request, 'myportfolio/contacto_formulario.html', {'form': form})

# Vista para ver el detalle de un contacto específico, requiere autenticación
@login_required
def contacto_detalle(request, pk):
    # Obtiene el contacto con la clave primaria especificada, o retorna 404 si no se encuentra
    contacto = get_object_or_404(Contacto, pk=pk)
    # Renderiza la plantilla 'contacto_detalle.html' pasando el contacto como contexto
    return render(request, 'myportfolio/contacto_detalle.html', {'contacto': contacto})

# Vista para editar un contacto específico, requiere autenticación
@login_required
def contacto_editar(request, pk):
    # Obtiene el contacto con la clave primaria especificada, o retorna 404 si no se encuentra
    contacto = get_object_or_404(Contacto, pk=pk)
    # Si la solicitud es de tipo POST, se procesa el formulario
    if request.method == "POST":
        # Se crea una instancia del formulario con los datos enviados y el contacto existente
        form = ContactoForm(request.POST, instance=contacto)
        # Si el formulario es válido, se guarda el contacto editado
        if form.is_valid():
            form.save()
            # Redirige a la vista de detalle del contacto
            return redirect('contacto_detalle', pk=contacto.pk)
    else:
        # Si la solicitud no es POST, se crea un formulario con los datos del contacto existente
        form = ContactoForm(instance=contacto)
    # Renderiza la plantilla 'contacto_editar.html' pasando el formulario como contexto
    return render(request, 'myportfolio/contacto_editar.html', {'form': form})

# Vista para eliminar un contacto específico, requiere autenticación
@login_required
def contacto_eliminar(request, pk):
    # Obtiene el contacto con la clave primaria especificada, o retorna 404 si no se encuentra
    contacto = get_object_or_404(Contacto, pk=pk)
    # Elimina el contacto
    contacto.delete()
    # Redirige a la vista de lista de contactos
    return redirect('contacto_lista')

# Vista para listar todo0000s los contactos, requiere autenticación
@login_required
def contacto_lista(request):
    # Obtiene todos los objetos de la clase Contacto
    contactos = Contacto.objects.all()
    # Renderiza la plantilla 'contacto_lista.html' pasando los contactos como contexto
    return render(request, 'myportfolio/contacto_lista.html', {'contactos': contactos})

# Vista de confirmación de contacto
def contacto_confirmacion(request):
    # Renderiza la plantilla 'contacto_confirmacion.html'
    return render(request, 'myportfolio/contacto_confirmacion.html')
####################################################################
@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'proyecto_detalle.html', {'proyecto': proyecto})