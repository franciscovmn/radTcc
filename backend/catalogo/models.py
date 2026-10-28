from datetime import date

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


def validar_ano(valor):
    if valor > date.today().year:
        raise ValidationError("O ano não pode ser maior que o ano corrente.")


class Curso(models.Model):
    nome = models.CharField(max_length=120)
    sigla = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.sigla} - {self.nome}"


class Orientador(models.Model):
    nome = models.CharField(max_length=120)
    titulacao = models.CharField(max_length=40)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "orientador"
        verbose_name_plural = "orientadores"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "autor"
        verbose_name_plural = "autores"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class PalavraChave(models.Model):
    termo = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name = "palavra-chave"
        verbose_name_plural = "palavras-chave"
        ordering = ["termo"]

    def __str__(self):
        return self.termo


class Trabalho(models.Model):
    class Situacao(models.TextChoices):
        EM_ANDAMENTO = "em_andamento", "Em andamento"
        DEFENDIDO = "defendido", "Defendido"
        PUBLICADO = "publicado", "Publicado"

    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    ano = models.PositiveSmallIntegerField(validators=[validar_ano])
    data_defesa = models.DateField(null=True, blank=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    situacao = models.CharField(
        max_length=20, choices=Situacao.choices, default=Situacao.EM_ANDAMENTO
    )
    arquivo_pdf = models.URLField(blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name="trabalhos")
    orientador = models.ForeignKey(
        Orientador, on_delete=models.PROTECT, related_name="trabalhos"
    )
    coorientador = models.ForeignKey(
        Orientador,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="trabalhos_coorientados",
    )
    autores = models.ManyToManyField(Autor, related_name="trabalhos")
    palavras_chave = models.ManyToManyField(
        PalavraChave, blank=True, related_name="trabalhos"
    )
    cadastrado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="trabalhos_cadastrados",
    )

    class Meta:
        verbose_name = "trabalho"
        verbose_name_plural = "trabalhos"
        ordering = ["-ano", "titulo"]
        constraints = [
            models.UniqueConstraint(
                fields=["titulo", "curso", "ano"], name="trabalho_titulo_curso_ano_unico"
            )
        ]

    def __str__(self):
        return f"{self.titulo} ({self.ano})"
