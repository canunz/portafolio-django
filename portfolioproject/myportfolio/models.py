from django.db import models
from ckeditor.fields import RichTextField  #####################ETAPA 5
from .utils import encrypt_message, decrypt_message

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='proyectos/')
    descripcion = models.TextField()
    contenido = RichTextField()  # Campo de texto enriquecido#######ETAPA 5
    tecnologias = models.ManyToManyField(Tecnologia)
    link_sitio = models.URLField(max_length=200)
    link_repositorio = models.URLField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()  # Campo para el mensaje original
    mensaje_cifrado = models.TextField(default='')  # Campo para almacenar el mensaje cifrado
    fecha = models.DateTimeField(auto_now_add=True)  # Añade el campo de fecha

    def save(self, *args, **kwargs):
        # Cifra el mensaje antes de guardarlo
        self.mensaje_cifrado = encrypt_message(self.mensaje)
        super().save(*args, **kwargs)

    def get_mensaje(self):
        # Descifra el mensaje al recuperarlo
        return decrypt_message(self.mensaje_cifrado)

    def __str__(self):
        return self.nombre

