from rest_framework import mixins, viewsets

from .models import Photo
from .serializers import PhotoSerializer


class PhotoViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """
    """

    queryset = Photo.objects.filter(is_active=True)
    serializer_class = PhotoSerializer
