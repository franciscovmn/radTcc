import unicodedata
from datetime import date
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction
from rest_framework.authtoken.models import Token

from catalogo import dados_iniciais as dados
from catalogo.models import Autor, Curso, Orientador, PalavraChave, Trabalho


def slug(texto):
    sem_acento = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    return sem_acento.lower()


class Command(BaseCommand):
    help = "Carrega os dados de teste do catálogo. Pode ser executado mais de uma vez."

    @transaction.atomic
    def handle(self, *args, **options):
        usuarios = self.criar_usuarios()
        cursos = {
            sigla: Curso.objects.get_or_create(sigla=sigla, defaults={"nome": nome})[0]
            for nome, sigla in dados.CURSOS
        }
        orientadores = [
            Orientador.objects.get_or_create(
                email=email, defaults={"nome": nome, "titulacao": titulacao}
            )[0]
            for nome, titulacao, email in dados.ORIENTADORES
        ]
        palavras = [
            PalavraChave.objects.get_or_create(termo=termo)[0]
            for termo in dados.PALAVRAS_CHAVE
        ]

        proximo_autor = 0
        posicao_no_curso = {sigla: 0 for sigla in cursos}
        criados = 0

        for i, (titulo, sigla, ano, situacao, kws, n_autores, resumo) in enumerate(
            dados.TRABALHOS
        ):
            indices = dados.ORIENTADORES_POR_CURSO[sigla]
            pos = posicao_no_curso[sigla]
            posicao_no_curso[sigla] += 1
            orientador = orientadores[indices[pos % len(indices)]]
            coorientador = None
            if i % 5 == 0:
                coorientador = orientadores[indices[(pos + 1) % len(indices)]]

            autores = []
            for _ in range(n_autores):
                autores.append(self.autor(proximo_autor))
                proximo_autor += 1

            com_defesa = situacao != "em_andamento"
            trabalho, novo = Trabalho.objects.get_or_create(
                titulo=titulo,
                curso=cursos[sigla],
                ano=ano,
                defaults={
                    "resumo": resumo,
                    "situacao": situacao,
                    "orientador": orientador,
                    "coorientador": coorientador,
                    "data_defesa": date(ano, 3 + i % 6, 5 + i % 20) if com_defesa else None,
                    "nota": Decimal(f"{7 + (i * 7) % 31 / 10:.1f}") if com_defesa else None,
                    "arquivo_pdf": (
                        f"https://repositorio.ifpb.edu.br/tcc/{ano}-{i + 1:02d}.pdf"
                        if com_defesa
                        else ""
                    ),
                    "cadastrado_por": usuarios[i % len(usuarios)],
                },
            )
            if novo:
                trabalho.autores.set(autores)
                trabalho.palavras_chave.set([palavras[k] for k in kws])
                criados += 1

        self.stdout.write(self.style.SUCCESS(f"{criados} trabalhos criados."))
        for usuario in usuarios:
            token = Token.objects.get(user=usuario)
            self.stdout.write(f"{usuario.username}: token {token.key}")

    def criar_usuarios(self):
        usuarios = []
        for username, email, senha in dados.USUARIOS:
            usuario, novo = User.objects.get_or_create(
                username=username, defaults={"email": email, "is_staff": True}
            )
            if novo:
                usuario.set_password(senha)
                usuario.is_superuser = True
                usuario.save()
            Token.objects.get_or_create(user=usuario)
            usuarios.append(usuario)
        return usuarios

    def autor(self, i):
        nome = f"{dados.NOMES[i]} {dados.SOBRENOMES[i]}"
        primeiro = slug(dados.NOMES[i].split()[0])
        ultimo = slug(dados.SOBRENOMES[i].split()[-1])
        email = f"{primeiro}.{ultimo}@academico.ifpb.edu.br"
        return Autor.objects.get_or_create(email=email, defaults={"nome": nome})[0]
