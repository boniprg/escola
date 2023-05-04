from django.urls import path,include
from rest_framework import routers

# from .views import CursosAPIView, CursoAPIView, AvaliacoesAPIView
from .views import CursosAPIView, AvaliacoesAPIView

router = routers.DefaultRouter()
router.register(r'cursos',CursosAPIView)

urlpatterns = [
    path('', include(router.urls))

#    path('cursos/', CursosAPIView.as_view(), name='cursos'),
#    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
#    path('cursos/<int:pk>/', CursosAPIView.as_view(), name='curso'),
#    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
]
