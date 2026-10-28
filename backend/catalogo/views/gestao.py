from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from catalogo.models import Trabalho
from catalogo.serializers.gestao import TrabalhoGestaoSerializer


class TrabalhoGestaoViewSet(viewsets.ModelViewSet):
    """
    Cadastro e manutenção de trabalhos, em qualquer situação.

    O campo `cadastrado_por` é definido pelo token da requisição e não
    é aceito no corpo. Para publicar, o trabalho precisa ter nota e data de defesa.
    """

    serializer_class = TrabalhoGestaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["situacao", "ano", "curso"]

    def get_queryset(self):
        return Trabalho.objects.select_related(
            "curso", "orientador", "coorientador", "cadastrado_por"
        ).prefetch_related("autores", "palavras_chave")

    def perform_create(self, serializer):
        serializer.save(cadastrado_por=self.request.user)
