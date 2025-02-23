from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from django.conf import settings

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class GeneroTextual(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class GeneroLiterario(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome


class Item(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    autores = models.ManyToManyField(Autor)
    data_original = models.DateField(null=True, blank=True)
    ano_original = models.IntegerField()
    categorias = models.ManyToManyField(Categoria)
    generos_textuais = models.ManyToManyField(GeneroTextual)
    generos_literarios = models.ManyToManyField(GeneroLiterario)
    tipo = models.CharField(max_length=20, null=False)  # Livro, Artigo, Tese, Dissertação, etc.
    arquivo = models.FileField(upload_to='arquivos/', null=True, blank=True)
    data_adicao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Volume(models.Model):
    arquivo = models.ForeignKey(Item, related_name='volumes', on_delete=models.CASCADE)
    numero = models.IntegerField()
    titulo = models.CharField(max_length=100, null=False)
    data_publicacao = models.DateField()

    def __str__(self):
        return f'{self.titulo} - Volume {self.numero}'


class Usuario(AbstractUser):
    foto_de_perfil = models.ImageField(upload_to='fotos_de_perfil/', blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='biblioteca_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='biblioteca_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
    
    def perfil_preview(self):
        if self.foto_de_perfil:
            return mark_safe(f'<img src="{self.foto_de_perfil.url}">')
        else:
            foto_padrao_url = settings.STATIC_URL + 'images/usuario.png'
            return mark_safe(f'<img src="{foto_padrao_url}">')



