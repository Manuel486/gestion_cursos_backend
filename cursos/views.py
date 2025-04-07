from rest_framework import viewsets, permissions
from .models import Curso
from .serializers import CursoSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'activo', 
                openapi.IN_QUERY, 
                description="Filtrar cursos activos o inactivos",
                type=openapi.TYPE_STRING, 
                enum=['true', 'false'],
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        activo = self.request.query_params.get('activo')
        if activo is not None:
            queryset = queryset.filter(activo=activo.lower() == 'true')
        return queryset
