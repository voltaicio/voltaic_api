from rest_framework import mixins, viewsets

from .models import Post
from .serializers import PostSerializer


class PostViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    """
    """

    lookup_field = "slug"
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializer
