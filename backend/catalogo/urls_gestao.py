from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views.gestao import TrabalhoGestaoViewSet

router = DefaultRouter()
router.register('trabalhos', TrabalhoGestaoViewSet, basename='gestao-trabalho')

urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path('', include(router.urls)),
]
