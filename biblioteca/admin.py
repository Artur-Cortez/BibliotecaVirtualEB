from django.contrib import admin
from .models import *

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
class GeneroTextualAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
class GeneroLiterarioAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_original', 'ano_original')
    search_fields = ('titulo',)
    list_filter = ('data_original', 'ano_original')
    filter_horizontal = ('autores', 'categorias', 'generos_textuais', 'generos_literarios')
class VolumeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'numero', 'data_publicacao')
    search_fields = ('titulo',)
    list_filter = ('data_publicacao',)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_staff', 'is_active')}),
        ('Foto de perfil', {'fields': ('foto_de_perfil',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'foto_de_perfil')}
        ),
    )


admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(GeneroTextual, GeneroTextualAdmin)
admin.site.register(GeneroLiterario, GeneroLiterarioAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(Usuario, UsuarioAdmin)

