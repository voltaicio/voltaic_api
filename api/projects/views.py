from rest_framework import mixins, viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """
    """

    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
