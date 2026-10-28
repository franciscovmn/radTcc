from django.contrib import admin

from .models import Autor, Curso, Orientador, PalavraChave, Trabalho


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("sigla", "nome")


@admin.register(Orientador)
class OrientadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "titulacao", "email")
    search_fields = ("nome", "email")


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    search_fields = ("nome", "email")


@admin.register(PalavraChave)
class PalavraChaveAdmin(admin.ModelAdmin):
    search_fields = ("termo",)


@admin.register(Trabalho)
class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano", "curso", "situacao")
    list_filter = ("situacao", "ano", "curso")
    search_fields = ("titulo",)
    filter_horizontal = ("autores", "palavras_chave")
